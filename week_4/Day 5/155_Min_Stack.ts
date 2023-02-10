class MinStack {
  constructor() {
    this.head = null;
  }

  push(val) {
    this.head = !this.head /* Space O(1) */
      ? new Node(val, val, null)
      : new Node(val, Math.min(val, this.head.min), this.head);
  }

  pop() {
    this.head = this.head.next; /* Time O(1) */
  }

  top() {
    return this.head.val; /* Time O(1) */
  }

  getMin() {
    return this.head.min; /* Time O(1) */
  }
}

class Node {
  constructor(val, min, next) {
    this.val = val;
    this.min = min;
    this.next = next;
  }
}
