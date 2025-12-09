import javax.swing.JButton;
import javax.swing.JFrame;

public class JavaSwing {
    public JavaSwing() {
        JFrame jframe = new JFrame();
        jframe.setLayout(null);
        jframe.setSize(400, 400);
        jframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Ensure the application exits when the window is closed

        JButton jbutton = new JButton("Click Me");
        jbutton.setBounds(150, 150, 100, 50); // Set position and size (x, y, width, height)
        jframe.add(jbutton); // Add the button to the JFrame

        jframe.setVisible(true);
    }

    public static void main(String[] args) {
        new JavaSwing();
    }
}
