BankABM
=======

An agent based model of a simple banking system
model an economy as a population of individual people interacting with each other in commerce. I would like to start by building on an existing ABM model of a banking system. The model is conceptually simple. A number of individuals interact by either giving or taking money from one another. If any individual has excess money, they save it in a bank. If any individual owes money, they borrow it from a bank. The current model is implemented in the ABM simulation software NetLogo. I want to create a modified version of this model in Python. I want to use Python because it it will allow me to extend the model at a future date and use the wide range of data analytic software written in Python.  

Scenario : (adapted from the Net Logo model by Uri Wilensky)
This simulation models the creation of money in an economy through a private banking system. As most of the money in the economy is kept in banks but only little of it needs to be used (i.e. in cash form) at any one time, the banks need only keep a small portion of their savings on-hand for those transactions. This portion of the total savings is known as the banks' reserves.

The banks are then able to loan out the rest of their savings. The government sets a reserve ratio mandating how much of the banks' holdings must be kept in reserve at a given time. Only one bank is used in this model. This model demonstrates, the reserve ratio is the key determiner of how much money is created in the system.

The implementation. In each round, people interact with each other to simulate everyday economic activity. Each person randomly selects someone else and will either give the person two or five pounds, or no money at all. After this, people must then sort out the balance with the bank. If after a number of such interactions a person has excess money, they deposit in the bank. If however the person has negative money, they will take out a loan from the bank if funds are available to borrow  Otherwise the person maintains the negative balance until the next round. The bank will only lend money if it has more savings than the minimum required reserve.

