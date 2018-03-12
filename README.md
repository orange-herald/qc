# QueryClick Challenge
> Solving the 'add-commas-to-number' challenge three different ways.

This is my solution to the software challenge set by QueryClick as part of the selection process for the position of Graduate Software Engineer.

The challenge - to correctly insert thousands separators (',') into numbers - was open-ended with several possible solutions. I chose to implement three versions using different approaches.

The first solution uses the [Humanize](https://pypi.python.org/pypi/humanize) package to produce the answer with just a single line of code. This is possibly the best 'real-world' solution as it is concise and leverages existing, well-tested and debugged code.

The second solution uses regular expressions to determine the correct placement of the separators. Finally, to demonstrate my ability to think algorithimically, I developed my own implementation.

This takes the modulus of the number's string representation by 3 to determine the position of the first separator. I then generate a range of comma positions by specifying the final comma position as -4 (three characters from the end) with a step value of three. I also added handling for the obvious corner cases of floating-point and negative values.

<img src="res/queryclick_logo.svg" alt="" width="250">
    
## Installation


```sh
pip install -r requirements.txt
```

Run tests:

```sh
pytest
```

## Meta

Steven MacDiarmid – [@stevemacdiarmid](https://twitter.com/stevemacdiarmid) – stevenmacdiarmid@me.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/orange-herald/qc](https://github.com/orange-herald/)