def findPayment(loan, r, m):
    """Assumes: loan and r are floats, m an int, returns the monthly payment for a mortage of
    size loan at a monthly rate r for m months."""
    return loan*((r*(1 + r)**m)/((1 + r)**m - 1))


class Mortage(object):
    """Abstract class for building different kinds of mortages"""
    def __init__(self, loan, annRate, months):
        """Create a new mortage"""
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None  #description of mortage

    def makePayment(self):
        """Make a payment"""
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - reduction)

    def getTotalPaid(self):
        """Returm the total amount of paid so far"""
        return sum(self.paid)

    def __str__(self):
        return self.legend


class Fixed(Mortage):
    def __init__(self, loan, r, months):
        Mortage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r*100) + '%'


class FixedWithPts(Mortage):
    def __init__(self, loan, r, months, pts):
        Mortage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*pts/100.0]
        self.legend = 'Fixed, ' + str(r*100) + '%, ' + str(pts) + ' points'


class TwoRate(Mortage):
    def __int__(self, loan, r, months, teaserRate, teaserMonths):
        Mortage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12.0
        self.legend = str(teaserRate*100) + '% for ' + str(self.teaserMonths)\
                      + 'months, then ' + str(r*100) + '%'

    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.owed[ -1], self.rate, self.months - self.teaserMonths)
        Mortage.makePayment(self)


def compareMortages(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    for m in range(totMonths):
        mort.makePayment()
    for m in morts:
        print(m)
        print(' Total payments = $' + str(int(m.getTotalPaid())))

compareMortages(amt=200000, years=30, fixedRate=0.07, pts=3.25, ptsRate=0.05,
                varRate1=0.045, varRate2=0.095, varMonths=48)
