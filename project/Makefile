IDIR =../include
CC=gcc
CPP=clang
CCFLAGS=-I$(IDIR) -o2

ODIR=obj
LDIR =../lib

LIBS=-lm

_DEPS = hellomake.hpp
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

_OBJ = hellomake.o hellofunc.o 
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))


$(ODIR)/%.o: %.cpp $(DEPS)
	$(CC) -cpp -o $@ $< $(CCFLAGS) 

suffix: $(OBJ)
	$(CC) -o $@ $^ $(CCFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ 

