import csv

import matplotlib.pyplot as plt

filename1 = 'data/attack3V2.csv'
filename2 = 'data/attack3V3.csv'
# filename3 = 'data/attack1V3.csv'
# filenameV3 = 'data/V3.csv'
#
#
# with open(filenameV0) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     train_accs_V0, train_losses_V0, valid_accs_V0, valid_losses_V0, epochs = [], [], [], [], []
#     epoch = 1
#     flag = -1
#     num = 0
#     for row in reader:
#         # print(row)
#         # print(flag, num)
#         if flag == 1 and num % 2 == 1 and num > 2:
#             # print("success")
#             epochs.append(epoch)
#             epoch = epoch + 1
#             train_acc = float(row[0])
#             train_loss = float(row[1])
#             valid_acc = float(row[5])
#             valid_loss = float(row[6])
#             train_accs_V0.append(train_acc)
#             train_losses_V0.append(train_loss)
#             valid_accs_V0.append(valid_acc)
#             valid_losses_V0.append(valid_loss)
#         num = num + 1
#         flag = flag * -1
#
with open(filename1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    valid_accs_attack2_V2, epochs, tops = [], [], []
    num = 0
    epoch = 1
    for row in reader:
        # print(row)
        # print(flag, num)
        if num > 0:
            # print("success")
            valid_acc = float(row[3]) * 100
            valid_accs_attack2_V2.append(valid_acc)
            epochs.append(epoch)
            tops.append(100)
            epoch = epoch + 1
        num = num + 1


with open(filename2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    valid_accs_attack2_V3 = []
    num = 0
    for row in reader:
        # print(row)
        # print(flag, num)
        if num > 0:
            # print("success")
            valid_acc = float(row[3]) * 100
            valid_accs_attack2_V3.append(valid_acc)
        num = num + 1

# with open(filename3) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     valid_accs_attack1_V3 = []
#     num = 0
#     for row in reader:
#         # print(row)
#         # print(flag, num)
#         if num > 0:
#             # print("success")
#             valid_acc = float(row[3]) * 100
#             valid_accs_attack1_V3.append(valid_acc)
#         num = num + 1

# ori_acc_V1 = [0.9018, 0.9018, 0.9018, 0.9018, 0.9018, 0.9018, 0.9018, 0.9018, 0.9018, 0.9018]


plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.plot(epochs, tops, c='black', alpha=0.5)
ax.plot(epochs, valid_accs_attack2_V2, label="V2", c='red', alpha=0.5)
ax.plot(epochs, valid_accs_attack2_V3, label="V3", c='blue', alpha=0.5)
# ax.plot(epochs, valid_accs_attack1_V3, label="V3", c='green', alpha=0.5)

ax. legend(loc='upper left')

ax.set_title("各模型对attack3的抵抗效果", fontproperties="SimHei", fontsize=24)
ax.set_xlabel("epoch", fontproperties="SimHei", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("valid_acc(%)", fontproperties="SimHei", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()