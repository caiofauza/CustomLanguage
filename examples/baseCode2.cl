toolkit inputTest()
{
    show("door Input test. Type a number: ");
    x = door();
    recover inputTest x;
}

toolkit main()
{
    result = inputTest();
    show(result);
}