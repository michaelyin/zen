# distutils: language = c++
# distutils: sources = gmm.cc

cdef extern from "gmm.h":

    cdef cppclass GMM:
        GMM(char *model)
        void posterior(float *x, float *pr)

cdef class GMM_py:

    cdef GMM *_thisptr

    def __cinit__(self, char *model):
        print 'loading model from ', model
        self._thisptr = new GMM(model)
        if self._thisptr == NULL:
            raise MemoryError()

    def __dealloc__(self):
        if self._thisptr != NULL:
            del self._thisptr

    cpdef calc_posterior(self, float[::1] xv, float[::1] pr):
        self._thisptr.posterior(&xv[0], &pr[0])

