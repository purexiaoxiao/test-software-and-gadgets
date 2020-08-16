package com;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class FileChange {
    public String fileRead() throws Exception {
        BufferedReader bReader = new BufferedReader(new InputStreamReader(getClass().getResourceAsStream("/ºº×Ö±í")));
        StringBuilder sb = new StringBuilder();
        String s = "";
        while ((s = bReader.readLine()) != null)
            sb.append(String.valueOf(s) + "\n");
        bReader.close();
        String str = sb.toString();
        return str;
    }


}
