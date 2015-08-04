[转](http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=139134&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26sortid%3D311)
我感觉对于OOP设计问题，关键要和面试官进行讨论，弄清情景situation ，who will use it,
在这个situation都是有哪些对象，他们在干什么，他们之间是什么关系，然后一个对象一个对象的
去分析这个对象应有的属性，和行为。多和面试官讨论，越细致越好！如果可以使用什么单例，
或者factory method 来设计的话，multi threading, 就尽量的添加上这些东西。

elevator:. 
First ask the interviewer what kind of elevator?  there is only one elevator serving that 
building or multiple elevators serving the building simultaneously?
this situation is that: there is one elevator serving the building.  there are many floors 
in the buliding. Maybe there are some users in different floor pressing the button simultaneously. 
This results in some requests to RequestProcessCenter for processing. The  RequestProcessCenter 
figure out the first request that need to be processed in such an algorithm that the distance 
between target floor and current floor is shortest.
First describe the whole situation. and check it with your interviewer;
Second sketch out the main classes and methods on the whiteboard;
So we need the following classes:
public class User {
private name;
public pressButton(int toFloor) {
    Request req = new Request( toFloor);
    RequestProcessCenter  center = RequestProcessCenter.getInstance();
    center.addRequest(req);
}
}
public class Request {
    private int toFloor;
    public Request(int _toFloor) {
        toFloor = _toFloor;
}. from:  
public getToFloor() {
    return toFloor;
}
}
public class Elevator {
    public static Elevator instance = null;
    private int currentFloor;
    public static Elevator( ) {
        if (instance == null) {  // late loading and eager loading
                    // connection pool-google 1point3acres
            synchronized (Elevator.class) {
                instance = new Elevator();. 
}
}
return instance;
}
public getInstance() {
    if (instance == null) {
            synchronized (SingletonDemo.class) {
                instance = new Elevator();
}
}
return instance;
}
public getCurrentFloor() {
    return currentFloor;
}
public moveToTargetFloor(int toFloor) {
    currentFloor = toFloor;
}
public void moveUp();.
public void moveDown();
}
public RequestProcessCenter implements runnable {
    public LinkedList<Request> queue;
public RequestProcessCenter( ) {
        queue = new LinkedList<Request>( );
}
public void run() {
        while ( true ) {
            processRequest( ).
}
}
public void addRequest(Request request) {
    queue.add(request);
}. 
public void removeRequest(Request request) {. 
    queue.remove(request);
}
public Request getNextRequest( ) {
    Request shortestReq = null;
    int shortest = Integer.MAX_VALUE;
    int curFloor = Elevator.getInstance( ).getCurrentFloor( );. from: 1point3acres.com/bbs 
    for (Request item : queue) {
        int distance = Math.abs(curFloor - item.getToFloor( ) );
        if (distance < shortest) {
            shortest = distance;
            shortestReq = item;
}
}
return shortestReq;
}
public void processRequest( ) {. 
    Request req = getNextRequest( );
if (req != null) {
        int toFloor = req.getToFloor( );. 
        Elevator.getInstance.moveToTargetFloor( toFloor);
        queue.remove(req);
}. 
   
}
}
