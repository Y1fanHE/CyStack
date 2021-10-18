# distutils: language=c++

from libcpp.vector cimport vector
from cpython.ref cimport PyObject

class StackEmptyError(Exception):
    pass

class StackIndexError(Exception):
    pass

cdef class CyStack:
    """Stack implementation based on Cython
    """
    cdef vector[PyObject*] _c_stack

    cpdef int size(self):
        """Return the size of the stack
        """
        return self._c_stack.size()

    cpdef bint is_empty(self):
        """Check if the stack is empty
        """
        return self._c_stack.empty()

    cpdef object push(self, object val):
        """Push an item to the stack
        """
        self._c_stack.push_back(<PyObject*>val)
        return self

    cpdef object pop(self):
        """Pop an item from the stack
        """
        cdef PyObject* val
        if self._c_stack.empty():
            raise StackEmptyError
        val=self._c_stack.back()
        self._c_stack.pop_back()
        return <object>val

    cpdef object nth(self, int index):
        """Return n-th item of the stack
        """
        cdef PyObject* val
        if self._c_stack.empty():
            raise StackEmptyError
        val=self._c_stack[index]
        return <object>val

    cpdef list take(self, int n):
        """Return the top-n items of the stack
        """
        cdef int i
        cdef list lst = []
        if self._c_stack.empty():
            raise StackEmptyError
        for i in range(self._c_stack.size()-n, self._c_stack.size()):
            lst.append(<object>self._c_stack[i])
        return lst

    cpdef object top(self):
        """Return the top item of the stack
        """
        cdef PyObject* val
        if self._c_stack.empty():
            raise StackEmptyError
        val=self._c_stack.back()
        return <object>val

    cpdef object insert(self, int index, object val):
        """Insert an item to any index of the stack
        """
        self._c_stack.insert(self._c_stack.begin()+index, <PyObject*>val)
        return self

    cpdef object set_nth(self, int index, object val):
        """Set n-th item of the stack 
        """
        self._c_stack[index] = <PyObject*>val
        return self

    cpdef object flush(self):
        """Clear the stack
        """
        self._c_stack.clear()
        return self
