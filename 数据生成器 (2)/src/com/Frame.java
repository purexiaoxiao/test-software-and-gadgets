package com;

import java.awt.BorderLayout;
import java.awt.Desktop;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.FileDialog;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.filechooser.FileFilter;
import javax.swing.filechooser.FileNameExtensionFilter;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.awt.event.ActionEvent;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;
import javax.swing.JLabel;
import javax.swing.JOptionPane;

import java.awt.Font;
import java.awt.Toolkit;
import java.awt.Window;

    /**
     * @author 罗颂
     */
    public class Frame extends JFrame {

        /**
         * Create the frame.
         */
        static String AbsoutPath;
        private JPanel contentPane;
        private JTextField AbsPath;
        private JTextField dataNum;
        Frame frame;

        public int Start() throws ClassNotFoundException, UnsupportedLookAndFeelException, InstantiationException, IllegalAccessException {
            frame=new Frame();
            return 1;
        }

    public Frame() throws ClassNotFoundException, UnsupportedLookAndFeelException, InstantiationException, IllegalAccessException {
        UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();//获得当前屏幕的对象
        int width = (int) screenSize.getWidth();//用screenSize对象获取屏幕的长
        int height = (int) screenSize.getHeight();//用screenSize对象获取屏幕的宽
        setTitle("数据生成器");
        setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);
        setBounds(750, 350, 467, 247);
        contentPane = new JPanel();
        contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
        setContentPane(contentPane);
        contentPane.setLayout(null);

        JButton LetsGo = new JButton("Let's Go!!");
        LetsGo.setFont(new Font("黑体", Font.PLAIN, 15));
        LetsGo.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent var1) {

                if (AbsPath.getText().equals("") || dataNum.getText().equals(""))
                    JOptionPane.showMessageDialog(Frame.this, "输入不完全", "系统提示", JOptionPane.ERROR_MESSAGE);
                else {
                    try {
                        CreateScore.Path = AbsoutPath;
                        CreateScore.ExportExcel(getDataNum());
                        File file = new File(AbsoutPath);
                        if (file.exists() && AbsoutPath.equals("nullnull.xls") == false) {
                            JOptionPane.showMessageDialog(null, "导出成功,是否查看文件", "提示", JOptionPane.INFORMATION_MESSAGE);
                            Desktop.getDesktop().open(file);
                        }


                    } catch (Exception e) {
                        // TODO 自动生成的 catch 块
                        e.printStackTrace();
                    }
                }
            }
        });
        LetsGo.setBounds(59, 160, 141, 27);
        contentPane.add(LetsGo);

        AbsPath = new JTextField();

        AbsPath.setFont(new Font("微软雅黑", Font.PLAIN, 16));
        AbsPath.setEnabled(false);
        AbsPath.setBounds(14, 39, 186, 24);
        contentPane.add(AbsPath);
        AbsPath.setColumns(10);

        JLabel label = new JLabel("\u6587\u4EF6\u6307\u5B9A\u8DEF\u5F84");
        label.setFont(new Font("黑体", Font.PLAIN, 15));
        label.setBounds(14, 13, 103, 18);
        contentPane.add(label);

        JButton Look = new JButton("\u6D4F\u89C8");
        String AbsPath;

        Look.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent var1) {
                getPath();
            }
        });
        Look.setFont(new Font("黑体", Font.PLAIN, 15));
        Look.setBounds(247, 38, 121, 27);
        contentPane.add(Look);

        JLabel label_1 = new JLabel("\u8F93\u5165\u6570\u636E\u89C4\u6A21");
        label_1.setFont(new Font("黑体", Font.PLAIN, 15));
        label_1.setBounds(14, 85, 151, 18);
        contentPane.add(label_1);

        dataNum = new JTextField();
        dataNum.setFont(new Font("微软雅黑", Font.PLAIN, 16));
        dataNum.setBounds(14, 116, 121, 24);
        contentPane.add(dataNum);
        dataNum.setColumns(10);


        JButton Cancel = new JButton("Cancel");
        Cancel.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent var1) {

                //System.exit(0);

            }
        });
        Cancel.setFont(new Font("黑体", Font.PLAIN, 15));
        Cancel.setBounds(247, 160, 113, 27);
        contentPane.add(Cancel);

        JLabel lblexcel = new JLabel("\u8BF7\u6CE8\u610FExcel\u6781\u9650\u884C\u6570\u4E3A1048576");
        lblexcel.setHorizontalAlignment(SwingConstants.CENTER);
        lblexcel.setFont(new Font("黑体", Font.PLAIN, 15));
        lblexcel.setBounds(195, 115, 240, 27);
        contentPane.add(lblexcel);
    }

    /**
     * Launch the application.
     *
     * @throws UnsupportedLookAndFeelException
     * @throws IllegalAccessException
     * @throws InstantiationException
     * @throws ClassNotFoundException
     */
    public static void main(String[] args) throws ClassNotFoundException, InstantiationException, IllegalAccessException, UnsupportedLookAndFeelException {


        Frame frame = new Frame();
        frame.setVisible(true);


    }

    public int getDataNum() {
        int DataNum = Integer.parseInt(dataNum.getText());
        return DataNum;
    }

    public void getPath() {
        try {
            FileDialog fd = new FileDialog(Frame.this, "导出到Excel表格", FileDialog.SAVE);
            FileFilter filefilter = new FileNameExtensionFilter("Excel表格文件(xls/xlsx)", "xls", "xlsx");

            fd.setLocation(500, 350);
            fd.setVisible(true);
            String stringfile = fd.getDirectory() + fd.getFile() + ".xls";
            AbsoutPath = stringfile;
            // System.out.println(AbsoutPath);
            File file = new File(stringfile);

            if (file.exists() && stringfile.equals("nullnull.xls") == false) {
                JOptionPane.showMessageDialog(null, "导出成功,是否查看文件", "提示", JOptionPane.INFORMATION_MESSAGE);
                Desktop.getDesktop().open(file);
            }
            //
        } catch (IOException ex) {
            ex.printStackTrace();
            JOptionPane.showMessageDialog(null, "导出失败", "错误", JOptionPane.ERROR_MESSAGE);
        } catch (Exception ex) {
            ex.printStackTrace();
            //JOptionPane.showMessageDialog(ChangeOrDeleteFrame.datatable, "导出失败","错误",JOptionPane.ERROR_MESSAGE);
        }
        AbsPath.setText(AbsoutPath);
    }


}
