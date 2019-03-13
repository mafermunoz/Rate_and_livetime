# Makefile for the ROOT test programs.
# This Makefile shows nicely how to compile and link applications
# using the ROOT libraries on all supported platforms.
#
# Copyright (c) 2000 Rene Brun and Fons Rademakers
#
# Author: Fons Rademakers, 29/2/2000


RC     := root-config
ifeq ($(shell which $(RC) 2>&2 | sed -ne "s@.*/$(RC)@$(RC)@p"),$(RC))
MKARCH := $(wildcard $(shell $(RC) --etcdir)/Makefile.arch)
RCONFIG := $(wildcard $(shell $(RC) --incdir)/RConfigure.h)
endif
ifneq ($(MKARCH),)
include $(MKARCH)
else
ifeq ($(ROOTSYS),)
ROOTSYS = ..
endif
include $(ROOTSYS)/etc/Makefile.arch
endif


#------------------------------------------------------------------------------


CXXFLAGS += -I $(DMPSWSYS)/include

LIBS += -L $(DMPSWSYS)/lib -lDmpEvent -lDmpService -lDmpEventFilter -lDmpKernel
#------------------------------------------------------------------------------


CLUMONIO       = rate.$(ObjSuf)
CLUMONIS       = rate.$(SrcSuf)
CLUMONI        = rate$(ExeSuf)


OBJS          = $(CLUMONIO)

PROGRAMS      = $(CLUMONI) $(CLUTRMONI)

ifeq ($(ARCH),aix5)
MAKESHARED    = /usr/vacpp/bin/makeC++SharedLib
endif

#------------------------------------------------------------------------------


.SUFFIXES: .$(SrcSuf) .$(ObjSuf) .$(DllSuf)
#.PHONY:    Aclock Hello Tetris

all:            $(PROGRAMS)


$(CLUMONI):     $(CLUMONIO)
		$(LD) $(LDFLAGS) $^ $(LIBS) $(OutPutOpt)$@
		echo $(LD) $(LDFLAGS) $^ $(LIBS) $(OutPutOpt)$@
		$(MT_EXE)
		@echo "$@ done"

$(CLUTRMONI):   $(CLUTRMONIO)
		$(LD) $(LDFLAGS) $^ $(LIBS) $(OutPutOpt)$@
		echo $(LD) $(LDFLAGS) $^ $(LIBS) $(OutPutOpt)$@
		$(MT_EXE)
		@echo "$@ done"

clean:
		@rm -f $(OBJS) $(TRACKMATHSRC) core *Dict.*



.SUFFIXES: .$(SrcSuf)

###



.$(SrcSuf).$(ObjSuf):
	$(CXX)  $(CXXFLAGS) -c $<
