# QueryClick Challenge
> Solving the 'add-commas-to-number' challenge three different ways.

This is my solution to the software challenge set by QueryClick as part of the interview process for the position of Graduate Software Engineer.

The challenge - to correctly insert thousands separators (',') into numbers - was open-ended with several possible solutions. I chose to implement three versions using different techniques.

The first solution uses the [Humanize](https://pypi.python.org/pypi/humanize) package to produce the answer with a single line of code. This is possibly the best 'real-world' solution as it leverages existing, well-tested and debugged code.

The second solution uses regular expressions to determine the correct placement of the separators. Finally, to demonstrate my ability to think algorithimacally, I developed my own implementation which uses modulus operation to determine the position of the first separator then generates a range of comma positions. 

![](res/queryclick_logo.svg)

## Installation


```sh
pip install requirements.txt
```

Run tests:

```sh
pytest
```

## Meta

Steven MacDiarmid – [@stevemacdiarmid](https://twitter.com/stevemacdiarmid) – stevenmacdiarmid@me.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/orange-herald/qc](https://github.com/orange-herald/)