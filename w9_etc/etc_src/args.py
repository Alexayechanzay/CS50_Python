def f(*args, **kwargs):
    print("Numbers:", args)
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25)
f(1,2,3)

### *args stores args in tuple data type.
### **kwargs stores args in dict data type.