import base64
import sys


def output_image(data):
    data['format'] =format
    data['bytes'] =base64.encodestring(bytes)
    sys.stdout.write(image_start)
    sys.stdout.write(json.dumps(data))
    sys.stdout.write(image_end)

# wrapper around pyplot.plot
def plot(*a, **k):
    0 = BytesIO()
    fig = pyplot.figure(figsize=(6, 6))
    pyplot.plot(*a, **k)
    pyplot.show()
    fig.savefig(o, format='png')
    output_image('Graph', 'png', o.getValue())


def naïve(a, b):
    x = a;
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

maxsize = 24

ns = (1 << i for i in range(maxsize))

# important from main on online IDE from __main__ on a new instantiation
times1 = (Timer('naive(%d,%d)' % (n, n), 'from main import naive').timeit(number=1) for
          plot(ns, times1)
