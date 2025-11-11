# TMUA Chapter 2 - Quiz 3: Counting and Probabilities Supplements S02 (Solutions)

**Time Allowed:** 90 minutes
**Number of Questions:** 20
**Difficulty:** ★★★☆

---

## Supplement Questions

### SQ1
**Problem:**
Anne, Bert, Clare, Derek and Emily are planning to play a game for which they need to divide themselves into three teams. Each team must have at least one member. The number of different ways they can do this is

**Options:**
- (A) 10
- (B) 15
- (C) 25
- (D) 30

**Solution:**
We need to partition 5 people into 3 non-empty groups. This is a Stirling number of the second kind problem, denoted S(5,3).

The possible group sizes are:
- 3, 1, 1: One team of 3, two teams of 1
- 2, 2, 1: Two teams of 2, one team of 1

**Case 1: Groups of size (3, 1, 1)**
- Choose 3 people for the first team: C(5,3) = 10 ways
- The remaining 2 people form two singleton teams
- Since the two singleton teams are indistinguishable, we don't divide by 2!
- Wait, teams are distinguishable by their members, not by labels
- If teams are unlabeled: C(5,3) = 10 ways

**Case 2: Groups of size (2, 2, 1)**
- Choose 2 people for first pair: C(5,2) = 10
- Choose 2 people from remaining 3: C(3,2) = 3
- The last person forms a singleton
- Since two pairs are indistinguishable: (10 × 3) / 2! = 30/2 = 15 ways

Total = 10 + 15 = 25 ways

**Answer: (C) 25**

---

### SQ2
**Problem:**
The faces of a cube are coloured red or blue. Exactly three are red and three are blue. The number of distinguishable cubes that can be produced (allowing the cube to be turned around) is?

**Options:**
- (A) 2
- (B) 4
- (C) 6
- (D) 20

**Solution:**
We need to count distinct colorings of a cube with 3 red faces and 3 blue faces, where two colorings are the same if one can be rotated into the other.

Using Burnside's lemma or by systematic enumeration:

Consider how the three red faces can be arranged:
1. **Three faces sharing a common vertex**: All three red faces meet at one corner - 1 way
2. **Three faces in a strip**: Three faces form a band around the cube - 1 way (opposite face arrangement)

Actually, let's think more carefully about the arrangements of 3 faces on a cube:
- Three faces can share a common vertex (meeting at a corner)
- Three faces can form an L-shape (two opposite edges)
- Three faces cannot all be mutually opposite (only 3 pairs of opposite faces)

After accounting for rotational symmetry:
- Three adjacent faces meeting at a vertex: 1 distinct coloring
- Three faces forming a band (no three sharing a vertex): 1 distinct coloring

Total distinguishable cubes = 2

**Answer: (A) 2**

---

### SQ3
**Problem:**
A grid of size 3 cm × 5 cm is drawn, ruled at 1 cm intervals. The number of squares that can be drawn using the grid is

**Options:**
- (A) 15
- (B) 18
- (C) 26
- (D) 37

**Solution:**
The grid has 4 horizontal lines and 6 vertical lines (creating 3 × 5 = 15 unit squares).

We can form squares of various sizes:

**1×1 squares:**
Number of positions: 3 × 5 = 15

**2×2 squares:**
- Horizontal positions: 3 - 1 = 2
- Vertical positions: 5 - 1 = 4
- Total: 2 × 4 = 8

**3×3 squares:**
- Horizontal positions: 3 - 2 = 1
- Vertical positions: 5 - 2 = 3
- Total: 1 × 3 = 3

**4×4 squares or larger:**
Not possible since the grid is only 3 cm tall.

Total = 15 + 8 + 3 = 26

**Answer: (C) 26**

---

### SQ4
**Problem:**
A cube painted black is cut into 125 identical cubes. How many of them are not painted at all?

**Options:**
- (A) 21
- (B) 25
- (C) 27
- (D) 30

**Solution:**
If the large cube is cut into 125 = 5³ identical small cubes, then each edge is divided into 5 equal parts.

The small cubes can be classified by position:
- **Corner cubes**: 8 cubes (3 faces painted)
- **Edge cubes** (not corners): 12 edges × 3 cubes per edge = 36 cubes (2 faces painted)
- **Face cubes** (not on edges): 6 faces × 9 cubes per face... wait, let me recalculate

Each face of the large cube is a 5×5 grid of small cube faces.
- Corner positions: 4 per face (but shared)
- Edge positions (not corners): 3 per edge
- Interior positions on face: (5-2)² = 9 per face

Interior cubes (not painted):
The unpainted cubes form a smaller cube inside, with edge length (5-2) = 3.
Number of unpainted cubes = 3³ = 27

**Answer: (C) 27**

---

### SQ5
**Problem:**
90 people enter a maze. At each junction a third will go left and two thirds will go right. After three such junctions, what is the most likely combination of turns people will have taken?

**Options:**
- (A) Gone right three times
- (B) Gone left three times
- (C) Gone right twice and once left
- (D) Gone twice left and once right
- (E) It is impossible to tell

**Solution:**
At each junction: P(left) = 1/3, P(right) = 2/3

For three junctions, we have outcomes with probabilities:
- **RRR** (right 3 times): (2/3)³ = 8/27
- **RRL, RLR, LRR** (right 2, left 1): 3 × (2/3)² × (1/3) = 3 × 4/9 × 1/3 = 12/27 = 4/9
- **RLL, LRL, LLR** (right 1, left 2): 3 × (2/3) × (1/3)² = 3 × 2/3 × 1/9 = 6/27 = 2/9
- **LLL** (left 3 times): (1/3)³ = 1/27

The probability for "right twice and left once" = 12/27 ≈ 0.444
The probability for "right three times" = 8/27 ≈ 0.296

The most likely combination is right twice and left once.

**Answer: (C) Gone right twice and once left**

---

### SQ6
**Problem:**
A bag contains *b* blue balls and *r* red balls. If two balls are picked at random and removed from the bag, what is the probability *P* that they are different colours?

**Options:**
- (A) 2*br* / [(*b* + *r*)(*b* + *r* − 1)]
- (B) *br* / [(*b* + *r*)(*b* + *r* − 1)]
- (C) *br* / (*b* + *r*)²
- (D) 2*br* / (*b* + *r*)²
- (E) 2*br*

**Solution:**
Total balls = *b* + *r*

The probability of picking two balls of different colors can happen in two ways:
1. Pick blue first, then red: P(BR) = *b*/(*b*+*r*) × *r*/(*b*+*r*−1)
2. Pick red first, then blue: P(RB) = *r*/(*b*+*r*) × *b*/(*b*+*r*−1)

P(different colors) = P(BR) + P(RB)
= *br*/[(*b*+*r*)(*b*+*r*−1)] + *rb*/[(*b*+*r*)(*b*+*r*−1)]
= 2*br*/[(*b*+*r*)(*b*+*r*−1)]

**Answer: (A) 2*br* / [(*b* + *r*)(*b* + *r* − 1)]**

---

### SQ7
**Problem:**
We wish to represent integer numbers by using our ten fingers. A finger is assumed to be either stretched out or curled up. How many different integers can we represent with our fingers?

**Options:**
- (A) 10
- (B) 512
- (C) 1000
- (D) 20
- (E) 1024

**Solution:**
Each finger has 2 possible states: stretched out or curled up.

With 10 fingers, the total number of different configurations is:
2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 = 2¹⁰ = 1024

Each configuration can represent a different integer, so we can represent 1024 different integers (typically 0 through 1023 in binary).

**Answer: (E) 1024**

---

### SQ8
**Problem:**
Ten students need to complete their compulsory practicals for their high school examinations as detailed in the table below:

| No. of students | No. of different practicals to complete |
|----------------|-----------------------------------------|
| 2              | 1                                       |
| 4              | 2                                       |
| 4              | 3                                       |

The school only has one laboratory in which several different experiments can be set up simultaneously. A maximum of six students are allowed in the school's laboratory for a lesson. Each practical takes one lesson. What is the minimum number of lessons required to complete all the practicals?

**Options:**
- (A) 3
- (B) 4
- (C) 5
- (D) 6
- (E) 10

**Solution:**
Total practical sessions needed:
- 2 students × 1 practical each = 2 sessions
- 4 students × 2 practicals each = 8 sessions
- 4 students × 3 practicals each = 12 sessions
- Total = 2 + 8 + 12 = 22 student-sessions

Since at most 6 students can be in the lab per lesson:
Minimum lessons = ⌈22/6⌉ = ⌈3.67⌉ = 4 lessons

However, we need to check if this is actually achievable given individual student requirements.

Let's verify a schedule:
- Lesson 1: All 4 "three-practical" students + 2 "two-practical" students = 6 students
- Lesson 2: Same 4 "three-practical" students + 2 "two-practical" students = 6 students
- Lesson 3: Same 4 "three-practical" students + 2 "one-practical" students = 6 students
- Lesson 4: Remaining 2 "two-practical" students can complete their second practical (2 students)

This works! Minimum = 4 lessons.

**Answer: (B) 4**

---

### SQ9
**Problem:**
To get to work, Sylvie first catches a bus and then catches a train.

- The probability that the bus is on time is 0.6.
- The probability that the bus is late is 0.4.
- If the bus is on time, then the probability that she will catch the train is 0.8.
- If the bus is late, then the probability that she will catch the train is 0.6.

Given that Sylvie catches the train, what is the probability that the bus was on time?

**Options:**
- (A) 1/3
- (B) 12/25
- (C) 2/5
- (D) 3/5
- (E) 2/3
- (F) 18/25
- (G) 6/7

**Solution:**
Let B = bus on time, T = catches train

Given:
- P(B) = 0.6, P(B') = 0.4
- P(T|B) = 0.8
- P(T|B') = 0.6

We need P(B|T) using Bayes' theorem:

P(B|T) = P(T|B) × P(B) / P(T)

First, find P(T):
P(T) = P(T|B) × P(B) + P(T|B') × P(B')
= 0.8 × 0.6 + 0.6 × 0.4
= 0.48 + 0.24
= 0.72

Now:
P(B|T) = (0.8 × 0.6) / 0.72
= 0.48 / 0.72
= 48/72
= 2/3

**Answer: (E) 2/3**

---

### SQ10
**Problem:**
I have two six-sided dice, each with faces numbered from 1 to 6. One of the dice is fair, but the other is not; it will land on numbers 1 to 5 with equal probability, but lands on 6 with a different probability.

When I roll the dice the probability that I get a total of 12 is 1/18.

What is the probability that I get a total of 2 when I roll the dice?

**Options:**
- (A) 1/72
- (B) 1/45
- (C) 1/36
- (D) 1/18
- (E) 1/9

**Solution:**
Let the fair die be F and the unfair die be U.
For F: P(i) = 1/6 for i = 1, 2, 3, 4, 5, 6

For U: Let P(1) = P(2) = P(3) = P(4) = P(5) = p, and P(6) = q
Since probabilities sum to 1: 5p + q = 1

To get a sum of 12, we need both dice to show 6:
P(sum = 12) = P(F=6) × P(U=6) = (1/6) × q = 1/18

Therefore: q = 1/3

From 5p + q = 1:
5p + 1/3 = 1
5p = 2/3
p = 2/15

To get a sum of 2, we need both dice to show 1:
P(sum = 2) = P(F=1) × P(U=1) = (1/6) × (2/15) = 2/90 = 1/45

**Answer: (B) 1/45**

---

### SQ11
**Problem:**
The ratio of the number of boys to the number of girls in a class is 1:3

The number of boys in the class is *n*.

Two students are chosen at random from the class.

The probability that both the students are boys is *p*.

Which one of the following is a correct expression for *n*, the number of boys in the class?

**Options:**
- (A) *n* = (3*p* − 1) / (9*p* − 1)
- (B) *n* = (3*p* + 1) / (9*p* − 1)
- (C) *n* = 1 / (1 − 9*p*)
- (D) *n* = 1 / (9*p* − 1)
- (E) *n* = (4*p* − 1) / (16*p* − 1)
- (F) *n* = (4*p* + 1) / (16*p* − 1)
- (G) *n* = 1 / (1 − 16*p*)
- (H) *n* = 1 / (16*p* − 1)

**Solution:**
Number of boys = *n*
Ratio boys:girls = 1:3, so number of girls = 3*n*
Total students = *n* + 3*n* = 4*n*

Probability that both students are boys:
*p* = C(*n*,2) / C(4*n*,2)
*p* = [*n*(*n*−1)/2] / [4*n*(4*n*−1)/2]
*p* = *n*(*n*−1) / [4*n*(4*n*−1)]
*p* = (*n*−1) / [4(4*n*−1)]

Now solve for *n*:
*p* × 4(4*n*−1) = *n* − 1
4*p*(4*n*−1) = *n* − 1
16*pn* − 4*p* = *n* − 1
16*pn* − *n* = 4*p* − 1
*n*(16*p* − 1) = 4*p* − 1
*n* = (4*p* − 1) / (16*p* − 1)

**Answer: (E) *n* = (4*p* − 1) / (16*p* − 1)**

---

### SQ12
**Problem:**
A bag contains only *n* red balls and 2*n* green balls.

One ball is picked and its colour recorded. It is then put back in the bag, and an additional ball of the same colour is added to the bag.

A second ball is then picked.

What is the probability that the two balls picked are not the same colour?

**Options:**
- (A) 2*n* / [3(3*n* − 1)]
- (B) 4*n* / [3(3*n* − 1)]
- (C) 5*n* / [3(3*n* − 1)]
- (D) (5*n* − 3) / [3(3*n* − 1)]
- (E) 2*n* / [3(3*n* + 1)]
- (F) 4*n* / [3(3*n* + 1)]
- (G) 5*n* / [3(3*n* + 1)]
- (H) (5*n* + 3) / [3(3*n* + 1)]

**Solution:**
Initial: *n* red, 2*n* green, total = 3*n* balls

**Case 1: First ball red, second ball green**
- P(first red) = *n*/(3*n*) = 1/3
- After replacing red and adding one red: (*n*+1) red, 2*n* green, total = 3*n*+1
- P(second green | first red) = 2*n*/(3*n*+1)
- P(RG) = (1/3) × [2*n*/(3*n*+1)] = 2*n* / [3(3*n*+1)]

**Case 2: First ball green, second ball red**
- P(first green) = 2*n*/(3*n*) = 2/3
- After replacing green and adding one green: *n* red, (2*n*+1) green, total = 3*n*+1
- P(second red | first green) = *n*/(3*n*+1)
- P(GR) = (2/3) × [*n*/(3*n*+1)] = 2*n* / [3(3*n*+1)]

P(different colors) = P(RG) + P(GR)
= 2*n*/[3(3*n*+1)] + 2*n*/[3(3*n*+1)]
= 4*n* / [3(3*n*+1)]

**Answer: (F) 4*n* / [3(3*n* + 1)]**

---

### SQ13
**Problem:**
A bag only contains 2*n* blue balls and *n* red balls. All the balls are identical apart from colour.

One ball is randomly selected and not replaced. A second ball is then randomly selected.

What is the probability that at least one of the selected balls is red?

**Options:**
- (A) (*n* − 1) / [3(3*n* − 1)]
- (B) (3*n* − 1) / [3(3*n* − 1)]
- (C) (4*n* − 2) / [3(3*n* − 1)]
- (D) 4*n* / [3(3*n* − 1)]
- (E) (5*n* − 1) / [3(3*n* − 1)]
- (F) (5*n* − 5) / [3(3*n* − 1)]

**Solution:**
Total balls = 2*n* + *n* = 3*n*

It's easier to use the complement: P(at least one red) = 1 − P(both blue)

P(both blue) = P(first blue) × P(second blue | first blue)
= (2*n*)/(3*n*) × (2*n*−1)/(3*n*−1)
= [2*n*(2*n*−1)] / [3*n*(3*n*−1)]
= (4*n*² − 2*n*) / [3*n*(3*n*−1)]
= 2*n*(2*n*−1) / [3*n*(3*n*−1)]
= 2(2*n*−1) / [3(3*n*−1)]
= (4*n*−2) / [3(3*n*−1)]

P(at least one red) = 1 − (4*n*−2) / [3(3*n*−1)]
= [3(3*n*−1) − (4*n*−2)] / [3(3*n*−1)]
= [9*n* − 3 − 4*n* + 2] / [3(3*n*−1)]
= (5*n* − 1) / [3(3*n*−1)]

**Answer: (E) (5*n* − 1) / [3(3*n* − 1)]**

---

### SQ14
**Problem:**
Two identical fair six-sided dice each have their faces numbered from 1 to 6, with one number on each face.

Both dice are thrown, and the number on each of the dice is recorded.

They are then both thrown again, and the number on each of the dice is recorded.

What is the probability that at least one of the four recorded numbers is even?

**Options:**
- (A) 1/4
- (B) 1/2
- (C) 9/16
- (D) 3/4
- (E) 15/16

**Solution:**
Use the complement: P(at least one even) = 1 − P(all four odd)

For a single die: P(odd) = 3/6 = 1/2, P(even) = 3/6 = 1/2

For four independent rolls:
P(all four odd) = (1/2) × (1/2) × (1/2) × (1/2) = 1/16

P(at least one even) = 1 − 1/16 = 15/16

**Answer: (E) 15/16**

---

### SQ15
**Problem:**
Eight people are sitting around a circular table, each holding a fair coin. All eight people flip their coins and those who flip heads stand while those who flip tails remain seated. What is the probability that no two adjacent people will stand?

**Options:**
- (A) 47/256
- (B) 3/16
- (C) 49/256
- (D) 25/128
- (E) 51/256

**Solution:**
Total possible outcomes = 2⁸ = 256

We need to count arrangements where no two adjacent people stand (flip heads).

Let *a*ₙ be the number of valid arrangements for *n* people in a circle where no two adjacent stand.

For a circle of 8 people, we can use the recurrence relation:
*a*ₙ = *a*ₙ₋₁ + *a*ₙ₋₂ for a line, but for a circle it's more complex.

For circular arrangements where no two adjacent positions are selected:
- If person 1 stands: person 2 and person 8 must sit
- If person 1 sits: standard problem for remaining 7

Using inclusion-exclusion or direct counting for circular arrangements:
For 8 positions in a circle with no two adjacent:

The formula is: *a*ₙ = *L*ₙ₋₁ + *L*ₙ₋₃ where *L* is Lucas number.
For n=8: L₇ + L₅ = 29 + 11 = 40

Wait, let me use another approach. For circular permutations:
Number of valid arrangements = *F*ₙ + *F*ₙ₋₂ where F is Fibonacci
Actually, for circular: answer is L_n (Lucas number)

For n=8: valid arrangements = 47

P(no two adjacent stand) = 47/256

**Answer: (A) 47/256**

---

### SQ16
**Problem:**
A choir director must select a group of singers from among his 6 tenors and 8 basses. The only requirements are that the difference between the number of tenors and basses must be a multiple of 4, and the group must have at least one singer. Let *N* be the number of groups that can be selected. What is the remainder when *N* is divided by 100?

**Options:**
- (A) 47
- (B) 48
- (C) 83
- (D) 95
- (E) 96

**Solution:**
Let *t* = number of tenors (0 ≤ *t* ≤ 6), *b* = number of basses (0 ≤ *b* ≤ 8)
Condition: |*t* − *b*| ≡ 0 (mod 4), which means *t* − *b* ≡ 0 (mod 4)
Also: *t* + *b* ≥ 1 (at least one singer)

So we need: *t* ≡ *b* (mod 4)

Count pairs (*t*, *b*):

**When *t* − *b* = 0:** *t* = *b* ∈ {0,1,2,3,4,5,6}
Pairs: (0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6) — but exclude (0,0)
Valid: 6 pairs

**When *t* − *b* = 4:** *t* = *b* + 4
- *b* = 0: *t* = 4 ✓
- *b* = 1: *t* = 5 ✓
- *b* = 2: *t* = 6 ✓
- *b* = 3: *t* = 7 ✗
- *b* = 4: *t* = 8 ✗
Valid: 3 pairs

**When *t* − *b* = −4:** *b* = *t* + 4
- *t* = 0: *b* = 4 ✓
- *t* = 1: *b* = 5 ✓
- *t* = 2: *b* = 6 ✓
- *t* = 3: *b* = 7 ✓
- *t* = 4: *b* = 8 ✓
- *t* = 5: *b* = 9 ✗
- *t* = 6: *b* = 10 ✗
Valid: 5 pairs

**When *t* − *b* = 8:** *t* = *b* + 8
Maximum *t* = 6, so no valid pairs.

**When *t* − *b* = −8:** *b* = *t* + 8
Maximum *b* = 8, so only *t* = 0, *b* = 8 ✓
Valid: 1 pair

Total pairs: 6 + 3 + 5 + 1 = 15

For each pair (*t*, *b*), number of ways = C(6, *t*) × C(8, *b*)

*N* = Σ C(6, *t*) × C(8, *b*)

Computing:
= C(6,1)C(8,1) + C(6,2)C(8,2) + C(6,3)C(8,3) + C(6,4)C(8,4) + C(6,5)C(8,5) + C(6,6)C(8,6)
+ C(6,4)C(8,0) + C(6,5)C(8,1) + C(6,6)C(8,2)
+ C(6,0)C(8,4) + C(6,1)C(8,5) + C(6,2)C(8,6) + C(6,3)C(8,7) + C(6,4)C(8,8)
+ C(6,0)C(8,8)

= 6×8 + 15×28 + 20×56 + 15×70 + 6×56 + 1×28
+ 15×1 + 6×8 + 1×28
+ 1×70 + 6×56 + 15×28 + 20×8 + 15×1
+ 1×1

= 48 + 420 + 1120 + 1050 + 336 + 28
+ 15 + 48 + 28
+ 70 + 336 + 420 + 160 + 15
+ 1

= 4095

*N* mod 100 = 4095 mod 100 = 95

**Answer: (D) 95**

---

### SQ17
**Problem:**
How many 15-letter arrangements of 5 A's, 5 B's and 5 C's have no A's in the first 5 letters, no B's in the next 5 letters and no C's in the last 5 letters?

**Options:**
- (A) Σ(k=0 to 5) C(5,k)³
- (B) 3⁵ · 2⁵
- (C) 2¹⁵
- (D) 15! / (5!)³
- (E) 3¹⁵

**Solution:**
Divide the 15 positions into three groups:
- Positions 1-5: can have B's or C's (not A's)
- Positions 6-10: can have A's or C's (not B's)
- Positions 11-15: can have A's or B's (not C's)

Let *k* be the number of B's in positions 1-5. Then:
- Positions 1-5 have *k* B's and (5−*k*) C's
- Positions 6-10 have (5−*k*) B's that must go here... wait, this is wrong.

Actually, let's say:
- *k* = number of B's in positions 1-5
- Then (5−*k*) C's in positions 1-5
- (5−*k*) B's must go in positions 11-15
- *k* C's must go in positions 6-10
- 5 A's must be distributed between positions 6-10 (5−*k* available) and 11-15 (5−(5−*k*)) = *k* available

For positions 1-5: Choose *k* positions for B's: C(5,*k*)
For positions 6-10: Choose positions for *k* C's among 5 positions: C(5,*k*), and remaining 5−*k* are A's
For positions 11-15: Choose positions for (5−*k*) B's among 5 positions: C(5,5−*k*) = C(5,*k*)

Total for each *k*: C(5,*k*) × C(5,*k*) × C(5,*k*) = C(5,*k*)³

Sum over all *k* from 0 to 5: Σ(*k*=0 to 5) C(5,*k*)³

**Answer: (A) Σ(k=0 to 5) C(5,k)³**

---

### SQ18
**Problem:**
How many odd positive 3-digit integers are divisible by 3 but do not contain the digit 3?

**Options:**
- (A) 96
- (B) 97
- (C) 98
- (D) 102
- (E) 120

**Solution:**
Conditions:
1. 3-digit number: 100 ≤ *n* ≤ 999
2. Odd: last digit ∈ {1, 5, 7, 9} (not 3 since we exclude 3)
3. Divisible by 3: sum of digits ≡ 0 (mod 3)
4. No digit 3: digits from {0, 1, 2, 4, 5, 6, 7, 8, 9}

Format: ABC where A ∈ {1,2,4,5,6,7,8,9}, B ∈ {0,1,2,4,5,6,7,8,9}, C ∈ {1,5,7,9}

For divisibility by 3: A + B + C ≡ 0 (mod 3)

Count by cases of C:

**C = 1** (sum ≡ 1 mod 3): Need A + B ≡ 2 (mod 3)
**C = 5** (sum ≡ 2 mod 3): Need A + B ≡ 1 (mod 3)
**C = 7** (sum ≡ 1 mod 3): Need A + B ≡ 2 (mod 3)
**C = 9** (sum ≡ 0 mod 3): Need A + B ≡ 0 (mod 3)

For A ∈ {1,2,4,5,6,7,8,9}:
- ≡ 0 (mod 3): {6,9} — 2 values
- ≡ 1 (mod 3): {1,4,7} — 3 values
- ≡ 2 (mod 3): {2,5,8} — 3 values

For B ∈ {0,1,2,4,5,6,7,8,9}:
- ≡ 0 (mod 3): {0,6,9} — 3 values
- ≡ 1 (mod 3): {1,4,7} — 3 values
- ≡ 2 (mod 3): {2,5,8} — 3 values

For A + B ≡ 0 (mod 3): (2×3) + (3×3) + (3×3) = 6 + 9 + 9 = 24 combinations
For A + B ≡ 1 (mod 3): (2×3) + (3×3) + (3×3) = 24 combinations
For A + B ≡ 2 (mod 3): (2×3) + (3×3) + (3×3) = 24 combinations

Total:
- C ∈ {1,7}: 2 × 24 = 48
- C ∈ {5}: 1 × 24 = 24
- C ∈ {9}: 1 × 24 = 24

Total = 48 + 24 + 24 = 96

**Answer: (A) 96**

---

### SQ19
**Problem:**
A pair of standard 6-sided fair dice is rolled once. The sum of the numbers rolled determines the diameter of a circle. What is the probability that the numerical value of the area of the circle is less than the numerical value of the circle's circumference?

**Options:**
- (A) 1/36
- (B) 1/12
- (C) 1/6
- (D) 1/4
- (E) 5/18

**Solution:**
Let *d* be the diameter (sum of dice).
- Area = π(*d*/2)² = π*d*²/4
- Circumference = π*d*

We need: π*d*²/4 < π*d*
Simplifying: *d*²/4 < *d*
*d*² < 4*d*
*d*² − 4*d* < 0
*d*(*d* − 4) < 0

Since *d* > 0, we need: *d* − 4 < 0, which means *d* < 4.

So we need the sum to be less than 4: sum ∈ {2, 3}

Possible outcomes:
- Sum = 2: (1,1) — 1 way
- Sum = 3: (1,2), (2,1) — 2 ways

Total favorable outcomes = 1 + 2 = 3
Total possible outcomes = 36

P = 3/36 = 1/12

**Answer: (B) 1/12**

---

### SQ20
**Problem:**
Chlo chooses a real number uniformly at random from the interval [0, 2017]. Independently, Laurent chooses a real number uniformly at random from the interval [0, 4034]. What is the probability that Laurent's number is greater than Chlo's number?

**Options:**
- (A) 1/2
- (B) 2/3
- (C) 3/4
- (D) 5/6
- (E) 7/8

**Solution:**
Let *C* be Chlo's number: *C* ~ Uniform[0, 2017]
Let *L* be Laurent's number: *L* ~ Uniform[0, 4034]

We need P(*L* > *C*).

The sample space is the rectangle [0, 2017] × [0, 4034] with area = 2017 × 4034.

The region where *L* > *C* is above the line *L* = *C* in this rectangle.

**Case 1:** When 0 ≤ *C* ≤ 2017 and *C* < *L* ≤ 4034

For a fixed *C* ∈ [0, 2017]:
- *L* ranges from *C* to 4034
- Length of favorable interval = 4034 − *C*

P(*L* > *C* | *C* = c) = (4034 − *c*) / 4034

P(*L* > *C*) = ∫₀²⁰¹⁷ [(4034 − *c*) / 4034] × [1/2017] d*c*
= (1 / (2017 × 4034)) ∫₀²⁰¹⁷ (4034 − *c*) d*c*
= (1 / (2017 × 4034)) [4034*c* − *c*²/2]₀²⁰¹⁷
= (1 / (2017 × 4034)) [4034 × 2017 − (2017)²/2]
= (1 / (2017 × 4034)) [2017 × 4034 − 2017²/2]
= (1 / (2017 × 4034)) × 2017[4034 − 2017/2]
= (1 / 4034) [4034 − 1008.5]
= 3025.5 / 4034
= 6051 / 8068
= 3025.5 / 4034

Let me recalculate:
= (1/4034)[4034 − 2017/2]
= (1/4034)[4034 − 1008.5]
= (1/4034) × 3025.5
= 3025.5/4034 = 6051/8068

Simplify: 4034 = 2 × 2017
6051/8068 = 6051/(4 × 2017)

Actually: 4034 − 2017/2 = (8068 − 2017)/2 = 6051/2
So: (6051/2) / 4034 = 6051 / 8068 = 3/4

**Answer: (C) 3/4**

---

*End of Solutions*
