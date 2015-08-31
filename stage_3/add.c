#include <Python.h>

static PyObject* add(PyObject* self, PyObject* args)   
{   
   int x=0;   
   int y=0;  
   int z=0;  
   if (!PyArg_ParseTuple(args, "i|i", &x, &y))  
   {
       perror("parse fail:");
       return NULL;  
   }

   z=x+y;  
   return Py_BuildValue("i", z);  
}   

static PyMethodDef addMethods[] =  
{   
   {"add",  add, METH_VARARGS, "Execute a shell command."},   
   {NULL, NULL, 0, NULL}  
};  

//PyMODINIT_FUNC initadd()   
void initadd(void)   
{   
    printf("initadd\n");
    PyObject *m;
    m = Py_InitModule("add", addMethods);   
    if (m == NULL) {
        perror("init fail:");
        return ;
    }
    else
    {
        printf("init ok\n");
    }

}   
