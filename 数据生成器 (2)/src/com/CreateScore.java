package com;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Random;

import javax.swing.JTable;
import javax.swing.table.TableModel;
/**
 * @author 罗颂
 * */

public class CreateScore {
	Random random=new Random(System.currentTimeMillis());
	
	static String ScoreTitle[]=new String[]{"姓名","c语言程序设计","python程序设计","高等数学","离散数学",	"线性代数","英语","形势与政策","概率与统计","总分"};
	static int score[]=new int[9];

	private  int times;
	
	static Object Message[]=new Object[10];
	
	/**创建带姓名列的Object数组*/
	public static Object[] crateMessage() throws Exception{
		int score[]=Line();
		Message[0]=ChineseName.Create();
		for(int i=0;i<9;i++)
		Message[i+1]=score[i];
		return Message;
	}

	/**创建一行整型数据*/
	public static int[] Line(){
		
			int sum = 0;
		for(int i=0;i<8;i++){
			score[i]=(int)(Math.random()*(40)+Math.random()*(60));
			sum=sum+score[i];
			}
		score[8]=sum;
		return score;
	}
	
	/**打表*/
	public  void PrintTable(int times) throws Exception{
		for(int i=0;i<times;i++){
			System.out.println(Arrays.toString(crateMessage()));
		}
	}
	
	/**把数组转成表格模型，本类中并未使用，鸡肋函数*/
	public static Object[][] ToExcelDataModel(int row) throws Exception{
		Object[][] RowAndCloumn=new Object[row][];
		for(int i=0;i<row;i++){
			Object object[]=crateMessage();
			RowAndCloumn[i]=object;
			}
		return RowAndCloumn;
	}
	
	/**把数据转成表格模型输出到Excel表格
	 * @throws Exception */
	
	public static String Path;
	
	 public static void ExportExcel(int row) throws Exception {
	        
	        final BufferedWriter bWriter = new BufferedWriter(new FileWriter(Path));
	        for(int t=0;t<ScoreTitle.length;t++)
	        {
	            bWriter.write(ScoreTitle[t].toString());
	            bWriter.write("\t");
	        }
	        bWriter.newLine();
	        for (int i = 0; i < row-1; i++) {
	        	
	        	Object object[]=crateMessage();
				
	        	for(int j=0;j<10;j++){
	        	bWriter.write(object[j].toString());
	            bWriter.write("\t");
	        	}
	        	bWriter.newLine();
	        }
	        
	        bWriter.close();

	    }
	 
	 public static void main(String[] args) throws Exception {
			//System.out.println(Arrays.toString(ScoreTitle));
			//new CreateScore().PrintTable(100000);
			new CreateScore().crateMessage();
			new CreateScore().ExportExcel(5000000);
		}
}
