'use client';
import React from 'react';
import { UploadOutlined } from '@ant-design/icons';
import { Button, message, Upload } from 'antd';

const props = {
  name: 'file',
  action: 'http://localhost:8000/upload',
  headers: {
    authorization: 'authorization-text',
  },
  async onChange(info) {
    if (info.file.status !== 'uploading') {
      console.log(info.file, info.fileList);
    }
    if (info.file.status === 'done') {
      message.success(`file uploaded successfully`);
    } else if (info.file.status === 'error') {
      message.error(`${info.file.name} file upload failed.`);
    }
  },
};

// file upload
const handleFileUploading = async () => {
    try {
      const res = await fetch('http://localhost:8000/upload');
      const data = await res.json();
      console.log(data)
      setResponseData(data); // Store the fetched data in state
    } catch (error) {
      console.error('Error uploading:', error);
    }
  };
const FileUpload = () => (
  <Upload {...props}>
    <Button icon={<UploadOutlined />}>Click to Upload</Button>
  </Upload>
);
export default FileUpload;