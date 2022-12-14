package locate.callgraph;

import org.apache.bcel.classfile.EmptyVisitor;
import org.apache.bcel.classfile.JavaClass;
import org.apache.bcel.classfile.Method;
import org.apache.bcel.generic.ConstantPoolGen;
import org.apache.bcel.generic.MethodGen;

import java.io.FileWriter;

public class ClassVisitor extends EmptyVisitor {
	private JavaClass clazz;
	private ConstantPoolGen constants;
	private String classReferenceFormat;
	private FileWriter des;

	public ClassVisitor(JavaClass jc, FileWriter fileWriter) {
		clazz = jc;
		constants = new ConstantPoolGen(clazz.getConstantPool());
		classReferenceFormat = "C:" + clazz.getClassName() + " %s";
		des = fileWriter;
	}

	public void visitJavaClass(JavaClass jc) {
		jc.getConstantPool().accept(this);
		Method[] methods = jc.getMethods();
		for (int i = 0; i < methods.length; i++)
			methods[i].accept(this);
	}

	public void visitMethod(Method method) {
		MethodGen mg = new MethodGen(method, clazz.getClassName(), constants);
		MethodVisitor visitor = new MethodVisitor(mg, clazz, des);
		visitor.start();
	}

	public void start() {
		visitJavaClass(clazz);
	}

}