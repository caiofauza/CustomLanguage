toolkit sum(a, b)
{   
    result = a+b;
    recover sum result;
}

toolkit print(a)
{
    show(a);
}

toolkit main()
{
    c = sum(1, 2);
    show(c);
    print(15);
}