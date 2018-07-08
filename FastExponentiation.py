def pow(x, n, d):
    if n <0:
        n = n+x
    if n==0:
        return 1%d
    else:
        R = pow(x,n//2,d)
        if n%2 ==0:
            return (R*R)%d
        else:
            return (R * R * x) % d;
