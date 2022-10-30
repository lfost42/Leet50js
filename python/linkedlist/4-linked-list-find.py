/*
Write a function, linkedListFind, that takes in the head of a 
linked list and a target value. The function should return a 
boolean indicating whether or not the linked list contains the 
target.

test_00:

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d

linkedListFind(a, "c"); // true
test_01:

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d

linkedListFind(a, "d"); // true
test_02:

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d

linkedListFind(a, "q"); // false
test_03:

const node1 = new Node("jason");
const node2 = new Node("leneli");

node1.next = node2;

// jason -> leneli

linkedListFind(node1, "jason"); // true
test_04:

const node1 = new Node(42);

// 42

linkedListFind(node1, 42); // true
test_05:

const node1 = new Node(42);

// 42

linkedListFind(node1, 100); // false
*/

/* SOLUTION */
const linkedListFind = (head, target) => {
  let current = head;
  while (current !== null) {
    if (current.val === target) return true;
    current = current.next;
  }
  return false;
};

/* EXPLANATION */
/*
We have a function linkedListFind that takes in head and target 
as parameters. Head is the head of our linked list and target is 
the value we are looking for. If we find our target in the linked
list, we return the boolean true and false if not. 
We begin by declaring a variable current and set it to the value 
of head. We begin a while loop to execute until current is not 
null. Then we check if current.val is equal to target and return 
true if it is. If not, we set current to current.next and 
continue. If current becomes null, we exit the while loop and 
return false. 
*/

