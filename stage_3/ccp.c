//#include <Akita/Akita.h>  
#include <Python.h>

int main() 
{
        Py_Initialize();    
        if (!Py_IsInitialized())  
            return -1;  
        PyRun_SimpleString("import sys");    
        PyRun_SimpleString("sys.path.append('./')");    
  
        //import Module  
        PyObject* pModule = PyImport_ImportModule("hello");    
        if (!pModule) {    
            print("Can't import Module!/n");
            return -1;    
        }    
  
        PyObject* pDict = PyModule_GetDict(pModule);    
        
        if (!pDict) {    
                return -1;    
        }    
  
        //fetch Function  
        PyObject* pFunHi = PyDict_GetItemString(pDict, "display");    
        PyObject_CallFunction(pFunHi, "s", "Crazybaby");    
        Py_DECREF(pFunHi);    
  
        //Release  
        Py_DECREF(pModule);    
        Py_Finalize();    
        return 0;    
}  
