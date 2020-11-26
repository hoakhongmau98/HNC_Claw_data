26.11.2020
THông báo này được viết bằng Tiếng Mẹ đẻ.
Thay đổi tên của các thư mục, đồng thời thay đổi tên của các file csv\
Cây thư mục sẽ được sắp xếp như sau:
HNC_Claw:
- Categories/
    - Product/
        + name_product.csv
        + ...
    - Element/
        + name_element.csv
        + ...
    - Error/
        + name_error
        + ...
    - Category_classify/
        + name_category.csv
    - Img/
        + filename.img
        + ...
    - Ipynb file/
        + filename.ipynb
    - Test/
    
Categories: Cpu, Main, Case, Vga ...
Product: Thông tin của các danh mục chính với data là các sản phẩm thuộc Category đó.
Category_classify: Thông tin về các tính chất mà mỗi category có để phân loại product.
element: Thông tin của mỗi sản phẩm về những class mà nó được soi chiếu vào.
error: Với mỗi sản phẩm mà không có hình ảnh sẽ được coi là một sản phẩm lỗi.