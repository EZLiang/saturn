#!/bin/sh

if [ ! -d "build" ]
then
  mkdir "build" || exit 1
fi

rm -rf build/*
rm -f ../kissat.exe
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
cp ../makefile.in makefile

cd ..
rm -f build
make all
cp build/kissat.exe ../kissat.exe
