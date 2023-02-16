"""
A transaction is possibly invalid if:

the amount exceeds $1000, or; if it occurs within (and including) 60 minutes of another transaction with the same 
name in a different city. You are given an array of strings transaction where transactions[i] consists of 
comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"] Output: ["alice,20,800,mtv","alice,50,100,
beijing"] Explanation: The first transaction is invalid because the second transaction occurs within a difference of 
60 minutes, have the same name and is in a different city. Similarly, the second one is invalid too.

Link: https://leetcode.com/problems/invalid-transactions/

N.B: Fom the input, go ahead to define your method and argument(s) you suggest it should take.

"""
import collections
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transaction = [t.split(",") for t in transactions]
        transaction = sorted(transaction, key=lambda x: int(x[1]))
        invalid = set()
        store = collections.defaultdict(list)

        for i, transact in enumerate(transaction):
            name, time, amount, city = transact
            time, amount = int(time), int(amount)

            if amount > 1000:
                invalid.add(i)

            if name in store:
                j = len(store[name]) - 1

                while j >= 0 and time - int(transaction[store[name][j]][1]) <= 60:
                    if city != transaction[store[name][j]][3]:
                        invalid.add(i)
                        invalid.add(store[name][j])
                    j -= 1

            store[name].append(i)

        return [",".join(transaction[i]) for i in invalid]
