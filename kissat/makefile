all:
	$(MAKE) -C "/home/runner/saturn/kissat/build"
kissat:
	$(MAKE) -C "/home/runner/saturn/kissat/build" kissat
tissat:
	$(MAKE) -C "/home/runner/saturn/kissat/build" tissat
clean:
	rm -f "/home/runner/saturn/kissat"/makefile
	-$(MAKE) -C "/home/runner/saturn/kissat/build" clean
	rm -rf "/home/runner/saturn/kissat/build"
coverage:
	$(MAKE) -C "/home/runner/saturn/kissat/build" coverage
indent:
	$(MAKE) -C "/home/runner/saturn/kissat/build" indent
test:
	$(MAKE) -C "/home/runner/saturn/kissat/build" test
.PHONY: all clean coverage indent kissat test tissat
