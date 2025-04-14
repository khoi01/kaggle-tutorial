

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    
    @abstractmethod
    def pay(self,amount:float):
        pass
    
class CreditCard(PaymentMethod):
    def pay(self, amount:float):
        return f"Paid ${amount} with Credit Card"

class Paypal(PaymentMethod):
    def pay(self, amount:float):
        return f"Paid ${amount} via PayPal"

class PaymentFailedError(Exception):
    """Raised when payment could not be completed."""
    def __init__(self,reason:float):
        super().__init__(f"Payment failed: {reason}")
        self.reason = reason


def process_payment(payment_method,amount):
    if(amount<=0):
        raise PaymentFailedError("Invalid payment amount.")
    print(payment_method.pay(amount))
    
    
    

class Exported(ABC):
    @abstractmethod
    def export(self,data):
        pass

class PDFExporter(Exported):
    def export(self,data):
        return f"Exported {data} as PDF"
    
class CSVExporter(Exported):
    def export(self, data):
        return f"Exported {data} as CSV"

def run_export(exported:Exported,data:str):
    print(exported.export(data))




def main():
    
    try:
        paypal = Paypal()
        process_payment(paypal,200)
        process_payment(paypal,-20)
    except PaymentFailedError as e:
        print("!",e)
    
    # pdf = PDFExporter()
    # csv = CSVExporter()
    
    # run_export(pdf,"Report")
    # run_export(csv,"Invoice")





if __name__ == '__main__':
    main()

