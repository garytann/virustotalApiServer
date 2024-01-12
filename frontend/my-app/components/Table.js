'use client';

import React from 'react';
import { Space, Table, Tag } from 'antd';
const { Column, ColumnGroup } = Table;


const DataTable = ({ data }) => (
  <Table dataSource={data}>
    <Column title="ID" dataIndex="id" key="id" />
    <Column title="File" dataIndex="fileName" key="fileName" />
    <Column title="SHA256" dataIndex="fileHash" key="fileHash" />
    <Column title="Detected" dataIndex="detected" key="detected" />
    <Column title="Date" dataIndex="date" key="date" />
  </Table>
);
export default DataTable;