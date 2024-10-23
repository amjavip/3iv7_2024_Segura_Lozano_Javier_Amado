import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculadoraGUI extends JFrame implements ActionListener {
    // Variables para los botones y la pantalla
    private JTextField pantalla;
    private double num1 = 0, num2 = 0, resultado = 0;
    private char operador;

    public CalculadoraGUI() {
        // Configuración de la ventana
        setTitle("Calculadora");
        setSize(400, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        // Pantalla donde se muestra el resultado
        pantalla = new JTextField();
        pantalla.setEditable(false);
        pantalla.setHorizontalAlignment(JTextField.RIGHT);
        pantalla.setFont(new Font("Arial", Font.BOLD, 30));
        add(pantalla, BorderLayout.NORTH);

        // Panel para los botones
        JPanel panelBotones = new JPanel();
        panelBotones.setLayout(new GridLayout(4, 4, 10, 10));

        // Arreglo de los botones de la calculadora
        String[] botones = {
                "7", "8", "9", "/",
                "4", "5", "6", "*",
                "1", "2", "3", "-",
                "0", "C", "=", "+"
        };

        // Crear y agregar los botones al panel
        for (String boton : botones) {
            JButton button = new JButton(boton);
            button.setFont(new Font("Arial", Font.BOLD, 24));
            button.addActionListener(this); // Agregamos el ActionListener para detectar clics
            panelBotones.add(button);
        }

        add(panelBotones, BorderLayout.CENTER);
    }

    // Acción cuando se pulsa un botón
    @Override
    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();

        if (command.charAt(0) >= '0' && command.charAt(0) <= '9') {
            pantalla.setText(pantalla.getText() + command);
        } else if (command.equals("C")) {
            pantalla.setText("");
        } else if (command.equals("=")) {
            num2 = Double.parseDouble(pantalla.getText());
            calcular();
            pantalla.setText(String.valueOf(resultado));
        } else {
            operador = command.charAt(0);
            num1 = Double.parseDouble(pantalla.getText());
            pantalla.setText("");
        }
    }

    // Método para realizar la operación
    private void calcular() {
        switch (operador) {
            case '+':
                resultado = num1 + num2;
                break;
            case '-':
                resultado = num1 - num2;
                break;
            case '*':
                resultado = num1 * num2;
                break;
            case '/':
                if (num2 != 0) {
                    resultado = num1 / num2;
                } else {
                    pantalla.setText("Error");
                }
                break;
        }
    }

    public static void main(String[] args) {
        // Crear y mostrar la calculadora
        CalculadoraGUI calculadora = new CalculadoraGUI();
        calculadora.setVisible(true);
    }
}
