import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import pyerrors as pe
import pyerrors.input.openQCD as qcdin
import pyerrors.input.sfcf as sfin
import shutil
import pytest

from time import sleep

def build_test_environment(type, cfgs, reps):
    if type == "o":
        for i in range(2,cfgs+1):
            shutil.copytree("data/sfcf_test/data_o/test_r0/cfg1","data/sfcf_test/data_o/test_r0/cfg"+str(i))
        for i in range(1,reps):
            shutil.copytree("data/sfcf_test/data_o/test_r0", "data/sfcf_test/data_o/test_r"+str(i))
    elif type == "c":
        for i in range(2,cfgs+1):
            shutil.copy("data/sfcf_test/data_c/data_c_r0/data_c_r0_n1","data/sfcf_test/data_c/data_c_r0/data_c_r0_n"+str(i))
        for i in range(1,reps):
            os.mkdir("data/sfcf_test/data_c/data_c_r"+str(i))
            for j in range(1,cfgs+1):
                shutil.copy("data/sfcf_test/data_c/data_c_r0/data_c_r0_n1","data/sfcf_test/data_c/data_c_r"+str(i)+"/data_c_r"+str(i)+"_n"+str(j))




def clean_test_environment(type, cfgs, reps):
    if type == "o":
        for i in range(1,reps):
            shutil.rmtree("data/sfcf_test/data_o/test_r"+str(i))
        for i in range(2,cfgs+1):
            shutil.rmtree("data/sfcf_test/data_o/test_r0/cfg"+str(i))
    elif type == "c":
        for i in range(1,reps):
            shutil.rmtree("data/sfcf_test/data_c/data_c_r"+str(i))
        for i in range(2,cfgs+1):
            os.remove("data/sfcf_test/data_c/data_c_r0/data_c_r0_n"+str(i))

        
def test_o_bb():
    build_test_environment("o",5,3)
    f_1 = sfin.read_sfcf("data/sfcf_test/data_o", "test", "f_1",quarks="lquark lquark", wf = 0, wf2=0, version = "2.0", single = True)
    print(f_1)
    clean_test_environment("o",5,3)
    assert len(f_1) == 1
    assert f_1[0].value == 351.1941525454502
        
def test_o_bi():
    build_test_environment("o",5,3)
    f_A = sfin.read_sfcf("data/sfcf_test/data_o", "test", "f_A",quarks="lquark lquark", wf = 0, version = "2.0")
    print(f_A)
    clean_test_environment("o",5,3)
    assert len(f_A) == 3
    assert f_A[0].value == 65.4711887279723
    assert f_A[1].value == 1.0447210336915187
    assert f_A[2].value == -41.025094911185185
            
def test_o_bib():
    build_test_environment("o",5,3)
    f_V0 = sfin.read_sfcf("data/sfcf_test/data_o", "test", "F_V0",quarks="lquark lquark", wf = 0, wf2 = 0, version = "2.0", b2b = True)
    print(f_V0)
    clean_test_environment("o",5,3)
    assert len(f_V0) == 3
    assert f_V0[0] == 683.6776090085115
    assert f_V0[1] == 661.3188585582334
    assert f_V0[2] == 683.6776090081005

def test_c_bb():
    build_test_environment("c",5,3)
    f_1 = sfin.read_sfcf("data/sfcf_test/data_c", "data_c", "f_1", quarks="lquark lquark", wf = 0, wf2=0, version = "2.0c", single = True)
    print(f_1)
    clean_test_environment("c",5,3)
    assert len(f_1) == 1
    assert f_1[0].value == 351.1941525454502

def test_c_bi():
    build_test_environment("c",5,3)
    f_A = sfin.read_sfcf("data/sfcf_test/data_c", "data_c", "f_A", quarks="lquark lquark", wf = 0, version = "2.0c")
    print(f_A)
    clean_test_environment("c",5,3)
    assert len(f_A) == 3
    assert f_A[0].value == 65.4711887279723
    assert f_A[1].value == 1.0447210336915187
    assert f_A[2].value == -41.025094911185185

def test_c_bib():
    build_test_environment("c",5,3)
    f_V0 = sfin.read_sfcf("data/sfcf_test/data_c", "data_c", "F_V0",quarks="lquark lquark", wf = 0, wf2 = 0, version = "2.0c", b2b = True)
    print(f_V0)
    clean_test_environment("c",5,3)
    assert len(f_V0) == 3
    assert f_V0[0] == 683.6776090085115
    assert f_V0[1] == 661.3188585582334
    assert f_V0[2] == 683.6776090081005

def test_a_bb():
    build_test_environment("a",5,3)
    f_1 = sfin.read_sfcf("data/sfcf_test/data_a", "data_a", "f_1", quarks="lquark lquark", wf = 0, wf2=0, version = "2.0a", single = True)
    print(f_1)
    clean_test_environment("a",5,3)
    assert len(f_1) == 1
    assert f_1[0].value == 351.1941525454502

def test_a_bi():
    build_test_environment("a",5,3)
    f_A = sfin.read_sfcf("data/sfcf_test/data_a", "data_a", "f_A", quarks="lquark lquark", wf = 0, version = "2.0a")
    print(f_A)
    clean_test_environment("a",5,3)
    assert len(f_A) == 3
    assert f_A[0].value == 65.4711887279723
    assert f_A[1].value == 1.0447210336915187
    assert f_A[2].value == -41.02509491118518

def test_a_bib():
    build_test_environment("a",5,3)
    f_V0 = sfin.read_sfcf("data/sfcf_test/data_a", "data_a", "F_V0",quarks="lquark lquark", wf = 0, wf2 = 0, version = "2.0a", b2b = True)
    print(f_V0)
    clean_test_environment("a",5,3)
    assert len(f_V0) == 3
    assert f_V0[0] == 683.6776090085115
    assert f_V0[1] == 661.3188585582334
    assert f_V0[2] == 683.6776090081005