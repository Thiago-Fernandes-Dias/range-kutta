build:
	@docker build -t range-kutta .

exec:
	@docker run -it --rm -v `pwd`:/example range-kutta