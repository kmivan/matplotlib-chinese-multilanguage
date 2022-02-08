from matplotlib_multilanguage import set_font
from pylab import *

set_font()
plot(arange(1, 10), arange(1, 10) ** 2)
title("平方关系")
xlabel("$x$")
ylabel("$x^2$")
show()
