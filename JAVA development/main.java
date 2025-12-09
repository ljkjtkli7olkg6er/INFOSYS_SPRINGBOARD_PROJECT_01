
class Oops {
    int salary;
    string name;

    public int getsalary() {
        return salary;
    }

    public string getname() {
        return name;
    }

    public void  setname( string n) {
        name = n;
    }

}
public class main{
public static void main(String[] args) {
    Oops harry = new Oops();
 harry.setname("jay kumar");
    harry.getname();
    harry.salary = 43000;
    System.out.println(harry.getsalary());

 }}