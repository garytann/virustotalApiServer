// `app/dashboard/page.js` is the UI for the `/dashboard` URL
import DataTable from '@/components/Table'
import FileUpload from '@/components/FileUpload'

export default async function Page() {
  
  return (
    <div>
      <DataTable />
    </div>

  )
}