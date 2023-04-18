from sys import path

path.append(
    'C:\\Users\\camaj\\Documents\\Coding\\Python\\PCAP\\Package Testing\\packages')

import extra.good.best.sigma as sig  # noqa
import extra.good.alpha as alp  # noqa
from extra.iota import funI  # noqa
from extra.good.beta import funB  # noqa

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())
