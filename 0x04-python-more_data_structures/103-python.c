#include <Python.h>

void print_python_list(PyObject *p)
void print_python_bytes(PyObject *p)

{
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

{
    Py_ssize_t size, i;
    char *buffer;

    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    buffer = PyBytes_AsString(p);
    printf("[.] bytes object info\n");
    printf("size: %ld\n", size);
    printf("trying string: %s\n", buffer);

    printf("first %ld bytes: ", size + 1 < 10 ? size + 1 : 10);
    for (i = 0; i < size + 1 && i < 10; i++)
    {
        printf("%02x ", buffer[i] & 0xff);
    }
    printf("\n");
}
