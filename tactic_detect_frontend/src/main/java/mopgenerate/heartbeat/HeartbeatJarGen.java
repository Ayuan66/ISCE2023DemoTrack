package mopgenerate.heartbeat;

import mopgenerate.JarGen;
import mopgenerate.util.HeartbeatCommand;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;

public class HeartbeatJarGen implements JarGen {

    @Override
    public void GenJar(String path) throws IOException, InterruptedException {
        File dir = new File(path);

        HeartbeatCommand command = new HeartbeatCommand();

        File f = new File(dir,"classes"+File.separator+"mop");
        if(!f.exists()) {
            f.mkdirs();
        }
        boolean isWindows = System.getProperty("os.name").toLowerCase().startsWith("windows");
        if (isWindows) {
            Process p = Runtime.getRuntime().exec("cmd /c " + command.mop, null, dir);
            p.waitFor();
            p = Runtime.getRuntime().exec("cmd.exe /c " + command.rvm, null, dir);
            p.waitFor();
            p = Runtime.getRuntime().exec("cmd.exe /c " + command.compile, null, dir);
            p.waitFor();
            p = Runtime.getRuntime().exec("cmd.exe /c " + command.jar, null, dir);
            p.waitFor();
        } else {
            InputStream resourceAsStream = this.getClass().getClassLoader().getResourceAsStream("bashScript/heartbeat.sh");
            File file = new File(dir + File.separator + "heartbeat.sh");
            if(file.exists()){
                file.delete();
            }
            FileWriter fileWriter = new FileWriter(file);
            int len = -1;
            while ((len = resourceAsStream.read())!=-1){
                fileWriter.write(len);
                fileWriter.flush();
            }
            fileWriter.close();

            Process p = Runtime.getRuntime().exec("/bin/sh heartbeat.sh", null, dir);
            p.waitFor();
        }

        String[] list = {"MultiSpec_1RuntimeMonitor.java","heartbeat.sh",
                "heartbeat.mop","heartbeatalive.mop","heartbeatlost.mop",
                "heartbeat.rvm","heartbeatalive.rvm","heartbeatlost.rvm"};
        //请教久昂具体用法
        for (String l:list) {
            JarGen.myDelete(path + File.separator + l);
        }
        JarGen.myDelete(path+File.separator+"classes");

        File file = new File(dir + File.separator + "MultiSpec_1MonitorAspect.aj");
        if (file.exists()){
            file.renameTo(new File(dir+File.separator+"heartbeat.aj"));
        } else {
            System.out.println("File rename failed!");
        }

        System.out.println("Jar Generated");
    }



}
