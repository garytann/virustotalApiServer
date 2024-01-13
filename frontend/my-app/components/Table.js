'use client';

import React from 'react';
import { Space, Table, Tag } from 'antd';
const { Column, ColumnGroup } = Table;
import { UploadOutlined } from '@ant-design/icons';
import { Button, message, Upload } from 'antd';

const props = {
    name: 'file',
    action: 'http://localhost:3000/api/upload',
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


export default function DataTable() {
    const [file, setFile] = React.useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    // handle the file upload
    const uploadFile = async () => {
        // e.preventDefault();
        try {
            const formData = new FormData();
            console.log(file)
            // formData.set('file', file);
            formData.append('file', file);
            // formData.append('file', file);
            const res = await fetch('/api/upload', {
                method: 'POST',
                // headers: {
                //     'Content-Type':'Multipart/form-data'
                //   },
                body: formData,
            });
            // const data = await res.json();
            console.log(res.text());
        } catch (error) {
            console.error('Error uploading:', error);
        }
    };

    return (
        <div>
            <Upload {...props}>
            {/* <Upload > */}
                <Button onSubmit={uploadFile} icon={<UploadOutlined />}>Click to Upload</Button>
            </Upload>


            <Table dataSource={''}>
                <Column title="ID" dataIndex="id" key="id" />
                <Column title="File" dataIndex="fileName" key="fileName" />
                <Column title="SHA256" dataIndex="fileHash" key="fileHash" />
                <Column title="Detected" dataIndex="detected" key="detected" />
                <Column title="Date" dataIndex="date" key="date" />
            </Table>

        </div>
    );

};
// export default DataTable;