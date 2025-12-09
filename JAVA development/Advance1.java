import java.awt.Button;
import java.awt.Color;
import java.awt.Frame;
import java.awt.Label;
import java.awt.TextField;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class Advance1 extends Frame {
    public void tutorial() {
        Frame frame = new Frame("New GUI");

        // creating and adding button into a frame
        Button button = new Button("Click Me");
        button.setBounds(80, 80, 80, 30);
        button.setBackground(Color.gray);
        frame.add(button);

        // creating label
        Label label =new Label("This label");
        label.setBounds(20,90,150,30);
        label.setBackground(Color.pink);
        frame.add(label);
        
        //creating field
        TextField textfield = new TextField();
        textfield.setBounds(20,120,150,30);
        frame.add(textfield);

        frame.setSize(400, 300);
        frame.setLayout(null);
        frame.setVisible(true);


        
        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                frame.dispose();
            }
        });
    }

    public static void main(String[] args) {
        Advance1 a = new Advance1();
        a.tutorial();
    }
}
