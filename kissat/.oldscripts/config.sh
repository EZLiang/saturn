#!/bin/sh

dir="`pwd|sed -e 's,.*/,,'`"

if [ ! -d "build" ]
then
  mkdir "build" || exit 1
fi

cd "build" || exit 1

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

rm -f makefile
sed \
  -e "s#@CC@#gcc#" \
  -e "s#@CFLAGS@#-W -Wall -O3 -DNEMBEDDED -DNDEBUG -DNMETRICS -DNSTATISTICS#" \
  -e "s#@LD@#gcc#" \
  -e "s#@AR@#ar#" \
  -e "s#@TESTDEFAULT@##" \
  ../makefile.in > makefile
