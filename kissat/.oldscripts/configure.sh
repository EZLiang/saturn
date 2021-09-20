#!/bin/sh

asan=no
check=unknown
check_all=no
check_heap=no
check_queue=no
check_vectors=no
compact=no
coverage=no
debug=no
default=no
extreme=no
embedded=unknown
logging=unknown
metrics=unknown
m32=no
options=yes
optimize=unknown
pedantic=unknown
profile=no
proofs=yes
quiet=no
sat=no
static=no
statistics=unknown
symbols=unknown
testdefault=unknown
ultimate=no
unsat=no

passthrough=""

msg () {
  echo "configure: $*"
}

if [ -t 1 ]
then
  BOLD="\033[1m"
  NORMAL="\033[0m"
  RED="\033[1;31m"
else
  BOLD=""
  NORMAL=""
  RED=""
fi

die () {
  echo "${BOLD}configure: ${RED}error:${NORMAL} $*" 1>&2
  exit 1
}

dir="`pwd|sed -e 's,.*/,,'`"

BUILD=build

if [ -d "$BUILD" ]
then
  msg "reusing existing build directory '$BUILD'"
else
  mkdir "$BUILD" || exit 1
  msg "new build directory '$BUILD'"
fi

cd "$BUILD" || exit 1

BUILD="`pwd`"
ROOT="`pwd|xargs dirname`"

cat <<EOF >../makefile
all:
	\$(MAKE) -C "$BUILD"
kissat:
	\$(MAKE) -C "$BUILD" kissat
tissat:
	\$(MAKE) -C "$BUILD" tissat
clean:
	rm -f "$ROOT"/makefile
	-\$(MAKE) -C "$BUILD" clean
	rm -rf "$BUILD"
coverage:
	\$(MAKE) -C "$BUILD" coverage
indent:
	\$(MAKE) -C "$BUILD" indent
test:
	\$(MAKE) -C "$BUILD" test
.PHONY: all clean coverage indent kissat test tissat
EOF

metrics=no
statistics=no
embedded=no
symbols=no
logging=no
check=no
CC=gcc

CFLAGS="-W -Wall -O3 -DNEMBEDDED -DNDEBUG -DNMETRICS - DNSTATISTICS"

msg "compiler '$CC $CFLAGS'"

LD="${CC}"
msg "linker '$LD' (no additional options)"

AR="ar"
msg "using default 'ar' (no cross compilation)"

testdefault=$debug

msg "no test programs added to default makefile goal"
TESTDEFAULT=""

rm -f makefile

sed \
  -e "s#@CC@#$CC#" \
  -e "s#@CFLAGS@#$CFLAGS#" \
  -e "s#@LD@#$LD#" \
  -e "s#@AR@#$AR#" \
  -e "s#@TESTDEFAULT@#$TESTDEFAULT#" \
  ./makefile.in > makefile
