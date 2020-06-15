/* @author: janani */

import java.io.File;
import java.io.IOException;
import jxl.Workbook;
import jxl.write.*;

public class GenerateStudentInfo {

    public static void main(String[] args) throws InterruptedException, IOException, WriteException {
        {

            //Create blank workbook
            WritableWorkbook workbook;

            String path = System.getProperty("user.dir");

            workbook = Workbook.createWorkbook(new File(path + "\\Students Info.xls "));

            WritableSheet wsheet = workbook.createSheet("First Sheet", 0);
            File folder = new File(path + "\\Final Paper Marking");
            File[] listOfFiles = folder.listFiles();

            Label label = new Label(0, 2, "A label record");

            for (int i = 0; i < listOfFiles.length; i++) {
                if (listOfFiles[i].isDirectory()) {

                    int cellid = 0;

                    String currencies = listOfFiles[i].getName();

                    //covert the entire filename to lowercase
                    String lowercasefilename = currencies.toLowerCase();
                    String Stlowercasefilename = lowercasefilename;
                    String StudentId = Stlowercasefilename.substring(0, 11);
                    StudentId = StudentId.replaceAll("\\s", "");
                    String[] Studentname = lowercasefilename.split(StudentId, 3);
                    label = new Label(cellid, i, StudentId.toUpperCase());
                    wsheet.addCell(label);
                    label = new Label(++cellid, i, Studentname[1].toUpperCase());
                    wsheet.addCell(label);
                }
            }

            workbook.write();
            workbook.close();
        }
    }
}
