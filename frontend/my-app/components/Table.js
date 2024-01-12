'use client';

import React from 'react';
import { Space, Table, Tag } from 'antd';
const { Column, ColumnGroup } = Table;
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
        message.error(`file upload failed.`);
      }
    },
  };
  // handle the file upload
  const onUpload = async (e) => {
    e.preventDefault();
    if (!file) return;
  
    const formData = new FormData();
    formData.append('file', file);
    try {
      const res = await fetch('http://localhost:8000/upload', {
        method: 'POST',
        body: formData,
      });
      const data = await res.json();
      console.log(data);
    } catch (error) {
      console.error('Error uploading:', error);
    }
  };

const DataTable = ({ data }) => (
    <div>
        
        <Upload {...props}>
            <Button onSubmit = {onUpload} icon={<UploadOutlined />}>Click to Upload</Button>
        </Upload>

        <Table dataSource={data}>
            <Column title="ID" dataIndex="id" key="id" />
            <Column title="File" dataIndex="fileName" key="fileName" />
            <Column title="SHA256" dataIndex="fileHash" key="fileHash" />
            <Column title="Detected" dataIndex="detected" key="detected" />
            <Column title="Date" dataIndex="date" key="date" />
        </Table>

    </div>

);
export default DataTable;