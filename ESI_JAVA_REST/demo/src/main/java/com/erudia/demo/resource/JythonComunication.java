package com.erudia.demo.resource;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;
	
public class JythonComunication {
	

	public JythonComunication() {
		// TODO Auto-generated constructor stub
	}
	
	public static String comunicar(int port,String msg) throws UnknownHostException, IOException{

		Socket s;
		s = new Socket("localhost",port);
		PrintWriter pw = new PrintWriter(s.getOutputStream());
		pw.println(msg);
		pw.flush();
		BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
		Scanner sc= new Scanner(br);
		String resp= sc.nextLine();
		sc.close();
		s.close();
		System.out.println(resp);
		return resp;
		
	}
	
	public static String SendToPython(IndexMannager im,String msg){

		while(true){
			try{
			return JythonComunication.comunicar(im.getIndex(),"resposta:msg"+msg);
			}catch(Exception e){
				System.out.println("COMUNICA��O FALHOU"+im.index);
				//im.BackIndex();
			}
		}
	};
	
		
		
		
		
	

}
