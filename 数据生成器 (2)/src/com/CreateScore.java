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
 * @author ����
 * */

public class CreateScore {
	Random random=new Random(System.currentTimeMillis());
	
	static String ScoreTitle[]=new String[]{"����","c���Գ������","python�������","�ߵ���ѧ","��ɢ��ѧ",	"���Դ���","Ӣ��","����������","������ͳ��","�ܷ�"};
	static int score[]=new int[9];

	private  int times;
	
	static Object Message[]=new Object[10];
	
	/**�����������е�Object����*/
	public static Object[] crateMessage() throws Exception{
		int score[]=Line();
		Message[0]=ChineseName.Create();
		for(int i=0;i<9;i++)
		Message[i+1]=score[i];
		return Message;
	}

	/**����һ����������*/
	public static int[] Line(){
		
			int sum = 0;
		for(int i=0;i<8;i++){
			score[i]=(int)(Math.random()*(40)+Math.random()*(60));
			sum=sum+score[i];
			}
		score[8]=sum;
		return score;
	}
	
	/**���*/
	public  void PrintTable(int times) throws Exception{
		for(int i=0;i<times;i++){
			System.out.println(Arrays.toString(crateMessage()));
		}
	}
	
	/**������ת�ɱ��ģ�ͣ������в�δʹ�ã����ߺ���*/
	public static Object[][] ToExcelDataModel(int row) throws Exception{
		Object[][] RowAndCloumn=new Object[row][];
		for(int i=0;i<row;i++){
			Object object[]=crateMessage();
			RowAndCloumn[i]=object;
			}
		return RowAndCloumn;
	}
	
	/**������ת�ɱ��ģ�������Excel���
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
