# Another point distance proof

Following on from the list at [Wikipedia](https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line#Proofs).

Say we have a line $l$ defined by:

$$
ax + by + c = 0
$$

Now say we have some point $Q = (x', y')$ where:

$$
ax' + by' + c = h
$$

What is the nearest perpendicular distance from the line $l$ to point $Q$?

First consider that the 2D line $l$ is on a 3D plane $p$ such that $z = ax + by
+ c$, where $z$ is the third height co-ordinate.

$l$ is the intersection of the plane $p$ with the $x, y$ plane where $z=0$.

There is also another line, call this $l'$, with formula $ax + by + c = h$, and
that is on the same plane $p$.


$l'$ is the intersection of the plane $p$ with a plane parallel to the $x, y$ plane
but where $z=h$.

Projecting $l'$ down to the $x, y$ plane gives a new line $l''$:

$$
ax + by + c - h = 0
$$

Notice that our point $Q$ ($x = x', y=y'$) satisfies that equation.

Call the projected point $Q'$ ($ax' + by' + c - h = 0$).

Now we have two parallel lines on the $x, y$ plane.

The vector $\vec{[a, b]}$ is perpendicular to the line $l$.  We can show this
because the vector $\vec{[a, b]}$ has a 0 dot product with any vector on line
$l$.

For example, select two points on line $l$: point $F$ where $x = 0$ and $G$
where $y = 0$.

For $F$, where we set $x = 0$:

$$
bx + c = 0 \implies y = \frac{-c}{b} \implies F = (0, \frac{-c}{b})
$$

For $G$, where we set $y = 0$:

$$
ax + c = 0 \implies x = \frac{-c}{a} \implies G = (\frac{-c}{a}, 0)
$$

$\vec{FG}$ = $G - F$ = $\vec{[\frac{-c}{a}, \frac{c}{b}]}$.

The dot product of $\vec{[a, b]}$ with $\vec{[\frac{-c}{a}, \frac{c}{b}]}$ is 0,
so $\vec{[a, b]}$ is orthogonal (perpendicular) to $l$.

Now imagine a vector, starting at $Q'$, with direction $\vec{[a, b]}$ that
intersects line $l$ at point $T = x_0, y_0$.  It is this vector that we use to
define the perpendicular (closest) distance between $(x', y')$ and $l$.

What scalar $e$ should we apply to $\vec{[a, b]}$, such that $(x', y') - e \vec{[a, b]} = (x_0, y_0)$?

We know that when $(x', y') - e \vec{[a, b]} = (x_0, y_0)$, these will be true:

$$
ax' + by' + c - h = 0
$$

$$
ax_0 + by_0 + c = 0 \
\implies a(x' - ea) + b(y' - eb) + c = 0
$$

Therefore:

$$
\begin{aligned}
ax' + by' + c - h = a(x' - ea) + b(y' - eb) + c \
\implies -h = -a^2e - b^2 e \
\implies e = \frac{h}{a^2 + b^2}
\end{aligned}
$$

We are interested in the length of the vector $\vec{Q'T}$ = $\vec{e [a, b]}$

The squared length of $\vec{Q'T}$ is $|| Q'T ||^2$ and:

$$
|| Q'T ||^2 = e^2 a^2 + e^2 b^2
$$

Substituting for $e$ above:

$$
|| Q'T ||^2 = [ \frac{h}{a^2 + b^2} ]^2 (a^2 + b^2) \
= \frac{h^2}{a^2 + b^2}
$$

and the length of this line, and therefore the distance we want, is:

$$
|| Q'T || = \frac{h}{\sqrt{a^2 + b^2}}
$$
