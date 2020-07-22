#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
 * Copyright 2019 by Samsung Eletrônica da Amazônia Ltda. Todos os direitos reservados.
 *
 * Este software e seus códigos são confidenciais ('Informações Confidenciais')
 * e de propriedade da Samsung Eletrônica da Amazônia Ltda.
 * Você não deverá divulgar as Informações Confidenciais e deverá utilizá-las apenas de acordo
 * com os termos do acordo de licença entre você e a Samsung Eletrônica da Amazônia Ltda.
 *
 * This software and its code is the confidential ('Confidential Information')
 * and proprietary information of Samsung Eletrônica da Amazônia Ltda.
 * You shall not disclose such Confidential Information and shall use it only in accordance
 * with the terms of the license agreement you entered into with Samsung Eletrônica da Amazônia Ltda.
 '''
import cv2
from time import sleep

teste = teste
print teste

class Camera:
    capture = None
    _instance= None

    @staticmethod
    def get_instance():
        if(Camera._instance == None):
            Camera._instance = Camera()
        return Camera._instance

    @staticmethod
    def get_current_frame():
        try:
            ret, frame = Camera.capture.read()
            return frame
        except:
            self.restart_camera()
            return None

    def __init__(self):
        self.camera_index = 0
        self.start_camera()

    def start_camera(self):
        try:
            Camera.capture = cv2.VideoCapture(self.camera_index)
            self.set_configs_camera()
        except:
            self.restart_camera()

    def set_configs_camera(self):
        Camera.capture.set(cv2.CAP_PROP_BUFFERSIZE, 3)
        Camera.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        Camera.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def restart_camera(self):
        Camera.capture.release()
        Camera.start_camera()
        sleep(1)


