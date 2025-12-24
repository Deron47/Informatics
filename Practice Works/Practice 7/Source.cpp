#include <Python.h>
#include <ctime>

static PyObject* calculate_mean(PyObject* self, PyObject* args) {
    PyObject* listObj;
    if (!PyArg_ParseTuple(args, "O", &listObj)) {
        return NULL;
    }

    long size = PyList_Size(listObj);
    double sum = 0;

    clock_t start = clock();

    for (int i = 0; i < size; i++) {
        PyObject* item = PyList_GetItem(listObj, i);
        sum += PyFloat_AsDouble(item);
    }

    double mean = 0;
    if (size > 0) {
        mean = sum / size;
    }

    clock_t end = clock();
    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;

    printf("C++ Time: %.5f\n", time_taken);

    return Py_BuildValue("d", mean);
}

static PyMethodDef MeanMethods[] = {
    {"calculate_mean", calculate_mean, METH_VARARGS, "Calculate arithmetic mean"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef meanmodule = {
    PyModuleDef_HEAD_INIT,
    "meanmod",
    "Module for calculating mean",
    -1,
    MeanMethods
};

PyMODINIT_FUNC PyInit_meanmod(void) {
    return PyModule_Create(&meanmodule);
}