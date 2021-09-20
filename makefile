all:
	$(MAKE) -C "/home/runner/iopx/build2"
kissat:
	$(MAKE) -C "/home/runner/iopx/build2" kissat
tissat:
	$(MAKE) -C "/home/runner/iopx/build2" tissat
clean:
	rm -f "/home/runner/iopx"/makefile
	-$(MAKE) -C "/home/runner/iopx/build2" clean
	rm -rf "/home/runner/iopx/build2"
coverage:
	$(MAKE) -C "/home/runner/iopx/build2" coverage
indent:
	$(MAKE) -C "/home/runner/iopx/build2" indent
test:
	$(MAKE) -C "/home/runner/iopx/build2" test
.PHONY: all clean coverage indent kissat test tissat
