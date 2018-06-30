CC = gcc
CFLAGS = -Wall
DEPS = strange_app.h
OBJ = strange_app.o $(shell date '+%B').o

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)


strange_app: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

clean:
	rm -f *.o
