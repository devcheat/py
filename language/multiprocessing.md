# __Python Multiprocessing__

Summary: To run code in parallel using the Python multiprocessing module.

# Introduction to the Python multiprocessing 
Generally, programs deal with two types of tasks:

- I/O-bound tasks: if a task does a lot of input/output operations, it’s called an I/O-bound task. Typical examples of I/O-bound tasks are reading from files, writing to files, connecting to databases, and making a network request. For I/O-bound tasks, you can use multithreading to speed them up.
- CPU-bound tasks: when a task does a lot of operations using a CPU, it’s called a CPU-bound task. For example, number calculation, image resizing, and video streaming are CPU-bound tasks. To speed up the program with lots of CPU-bound tasks, you use multiprocessing.

Multiprocessing allows two or more processors to simultaneously process two or more different parts of a program.

In Python, you use the `multiprocessing` module to implement multiprocessing.

## Python multiprocessing example 
See the following program:
```py
import time

def task():
    result = 0
    for _ in range(10**8):
        result += 1
    return result

if __name__ == '__main__':
    start = time.perf_counter()
    task()
    task()
    finish = time.perf_counter()

    print(f'It took {finish-start:.2f} second(s) to finish')
```
Output:
```
It took  5.55 second(s) to finish
```

### How it works.

First, define the task() function is a CPU-bound task because it performs a heavy computation by executing a loop for 100 million iterations and incrementing a variable result:
```py
def task():
    result = 0
    for _ in range(10**8):
        result += 1
    return result
```

Second, call the task() functions twice and record the processing time:
```py
if __name__ == '__main__':
    start = time.perf_counter()
    task()
    task()
    finish = time.perf_counter()

    print(f'It took {finish-start: .2f} second(s) to finish')
```

On our computer, it took 5.55 seconds to complete.

## Using multiprocessing module 
The following program uses the multiprocessing module but takes less time:

```py
import time
import multiprocessing

def task() -> int:
    result = 0
    for _ in range(10**8):
        result += 1
    return result

if __name__ == '__main__':
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()
    print(f'It took {finish-start:.2f} second(s) to finish')
```

Output:
```
It took  3.43 second(s) to finish
```

### How it works.

First, import the multiprocessing module:
```py
import multiprocessing
```
Second, create two processes and pass the task function to each:

```py
p1 = multiprocessing.Process(target=task)
p2 = multiprocessing.Process(target=task)
```
Note that the `Process()` constructor returns a new `Process` object.

Third, call the `start()` method of the `Process` objects to start the process:
```py
p1.start()
p2.start()
```
Finally, wait for the processes to complete by calling the join() method:
```py
p1.join()
p2.join()
```

## Python multiprocessing practical example 
We’ll use the multiprocessing module to resize the high-resolution images.

First, install the Pillow library for image processing:
```py
pip install Pillow
```
Second, develop a program that creates thumbnails of the pictures in the images folder and save them to the thumbs folder:

```py
import time
import os
from PIL import Image, ImageFilter

filenames = [
    'images/1.jpg',
    'images/2.jpg',
    'images/3.jpg',
    'images/4.jpg',
    'images/5.jpg',
]

def create_thumbnail(filename, size=(50,50), thumb_dir ='thumbs'):
    # open the image
    img = Image.open(filename)
    
    # apply the gaussian blur filter
    img = img.filter(ImageFilter.GaussianBlur())

    # create a thumbnail
    img.thumbnail(size)
    
    # save the image
    img.save(f'{thumb_dir}/{os.path.basename(filename)}')

    # display a message
    print(f'{filename} was processed...')


if __name__ == '__main__':
    start = time.perf_counter()

    for filename in filenames:
        create_thumbnail(filename)
        
    finish = time.perf_counter()

    print(f'It took {finish-start:.2f} second(s) to finish')
```
On our computer, it took about 4.06 seconds to complete:
```
images/1.jpg was processed...
images/2.jpg was processed...
images/3.jpg was processed...
images/4.jpg was processed...
images/5.jpg was processed...
It took 4.06 second(s) to finish
```


Third, modify the program to use multiprocessing. Each process will create a thumbnail for a picture:


```py
import time
import os
from PIL import Image, ImageFilter

import multiprocessing

filenames = [
    'images/1.jpg',
    'images/2.jpg',
    'images/3.jpg',
    'images/4.jpg',
    'images/5.jpg',
]

def create_thumbnail(filename, size=(50,50), thumb_dir ='thumbs'):
    # open the image
    img = Image.open(filename)
    
    # apply the gaussian blur filter
    img = img.filter(ImageFilter.GaussianBlur())

    # create a thumbnail
    img.thumbnail(size)
    
    # save the image
    img.save(f'{thumb_dir}/{os.path.basename(filename)}')

    # display a message
    print(f'{filename} was processed...')

def main():
    start = time.perf_counter()

    # create processes
    processes = [multiprocessing.Process(target=create_thumbnail, args=[filename]) 
                for filename in filenames]

    # start the processes
    for process in processes:
        process.start()

    # wait for completion
    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'It took {finish-start:.2f} second(s) to finish')


if __name__ == '__main__':
    main()
```
Output:
```
images/5.jpg was processed...
images/4.jpg was processed...
images/1.jpg was processed...
images/3.jpg was processed...
images/2.jpg was processed...
It took 2.92 second(s) to finish
```
In this case, the output shows that the program processed the pictures faster.

## Summary 
Use Python multiprocessing to run code in parallel to deal with CPU-bound tasks.


# **Python ProcessPoolExecutor**


**Summary**: To use the Python `ProcessPoolExecutor` to create and manage a process pool effectively.

Introduction to the Python ProcessPoolExecutor class [](https://www.pythontutorial.net/python-concurrency/python-processpoolexecutor/#introduction-to-the-python-processpoolexecutor-class "Anchor for Introduction to the Python ProcessPoolExecutor class")
----

[In the previous tutorial](https://www.pythontutorial.net/advanced-python/python-multiprocessing/), you learned how to run code in parallel by creating processes manually using the `Process` class from the `multiprocessing` module. However, manually creating processes is not efficient.

To manage the processes more efficiently, you can use a process pool. Like a [thread pool](https://www.pythontutorial.net/advanced-python/python-threadpoolexecutor/), a process pool is a pattern for managing processes automatically.

The `ProcessPoolExecutor` class from the `concurrent.futures` module allows you to create and manage a process pool.

For example, the `ProcessPoolExecutor` class uses the number of CPU cores for creating an optimized number of processes to create.

The `ProcessPoolExecutor` extends the `Executor` class that has three methods:

-   `submit()` -- dispatch a function to be executed by the process and return a Future object.
-   `map()` -- call a function to an iterable of elements.
-   `shutdown()` -- shut down the executor.

To release the resources held by the executor, you need to call the `shutdown()` method explicitly. To shut down the executor automatically, you can use a [context manager](https://www.pythontutorial.net/advanced-python/python-context-managers/).

The `Future` object represents an eventful result of an asynchronous operation. It has two main methods for getting the result:

-   `result()` -- return the result from the asynchronous operation.
-   `exception()` -- return an exception that occurred while running the asynchronous operation.

## Python ProcessPoolExecutor example


The following program uses a process pool to create thumbnails for pictures in the `images` folder and save them to the `thumbs` folder.

```py
import time
import os
from PIL import Image, ImageFilter

from concurrent.futures import ProcessPoolExecutor

filenames = [
    'images/1.jpg',
    'images/2.jpg',
    'images/3.jpg',
    'images/4.jpg',
    'images/5.jpg',
]

def create_thumbnail(filename, size=(50,50), thumb_dir ='thumbs'):
    # open the image
    img = Image.open(filename)

    # apply the gaussian blur filter
    img = img.filter(ImageFilter.GaussianBlur())

    # create a thumbnail
    img.thumbnail(size)

    # save the image
    img.save(f'{thumb_dir}/{os.path.basename(filename)}')

    # display a message
    print(f'{filename} was processed...')

def main():
    start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        executor.map(create_thumbnail, filenames)

    finish = time.perf_counter()

    print(f'It took {finish-start: .2f} second(s) to finish')

if __name__ == '__main__':
    main()`Code language: Python (python)
```


Output:

```
images/5.jpg was processed...
images/4.jpg was processed...
images/3.jpg was processed...
images/2.jpg was processed...
images/1.jpg was processed...
It took  0.79 second(s) to finish
```

Note that to run the program, you need to install the `Pillow` which is a popular library for image processing by running the pip command `pip install Pillow`.

How it works.

First, declare a list of files for creating thumbnails:

```py
filenames = [
    'images/1.jpg',
    'images/2.jpg',
    'images/3.jpg',
    'images/4.jpg',
    'images/5.jpg',
]
```


Second, define a function that creates a thumbnail from an image file and saves the output to the thumbnail folder:

```py
def create_thumbnail(filename, size=(50,50), thumb_dir ='thumbs'):
    # open the image
    img = Image.open(filename)

    # apply the gaussian blur filter
    img = img.filter(ImageFilter.GaussianBlur())

    # create a thumbnail
    img.thumbnail(size)

    # save the image
    img.save(f'{thumb_dir}/{os.path.basename(filename)}')

    # display a message
    print(f'{filename} was processed...')`Code language: Python (python)
```

Third, create a process pool and call the `create_thumbnail()` function for each picture specified in the filenames:

```py
with ProcessPoolExecutor() as executor:
    executor.map(create_thumbnail, filenames)`Code language: Python (python)

```
## Summary 


-   Use the Python ProcessPoolExecutor class to create and manage a process pool automatically.

